#!/usr/bin/env ruby
# Collect the facts one DataTalks.Club Weekly issue needs: running Zoomcamps
# (from the course platform), upcoming events, Book of the Week, new
# recordings, and new Alexey on Data posts.
#
# Usage (from the repository root):
#   ruby .claude/skills/dtc-newsletter/scripts/week_sources.rb --date 2026-09-28
#   ruby .claude/skills/dtc-newsletter/scripts/week_sources.rb --date 2026-09-28 --out newsletter/issues/<issue>/sources.md

require "cgi"
require "date"
require "json"
require "net/http"
require "optparse"
require "time"
require "uri"
require "yaml"

ROOT = File.expand_path("../../../..", __dir__)
PLATFORM = "https://courses.datatalks.club"
SITE_RAW = "https://raw.githubusercontent.com/DataTalksClub/datatalksclub.github.io/main"
SITE_API = "https://api.github.com/repos/DataTalksClub/datatalksclub.github.io"
FEED_URL = "https://alexeyondata.substack.com/feed"
DISPLAY_TZ = "Europe/Berlin"

# Platform slug prefix => GitHub repo and local course folder under courses/.
COURSES = {
  "ml-zoomcamp" => { repo: "DataTalksClub/machine-learning-zoomcamp", folder: "ml-zoomcamp" },
  "ai-dev-tools" => { repo: "DataTalksClub/ai-dev-tools-zoomcamp", folder: "ai-dev-tools-zoomcamp" },
  "llm-zoomcamp" => { repo: "DataTalksClub/llm-zoomcamp", folder: "llm-zoomcamp" },
  "de-zoomcamp" => { repo: "DataTalksClub/data-engineering-zoomcamp", folder: "de-zoomcamp" },
  "mlops-zoomcamp" => { repo: "DataTalksClub/mlops-zoomcamp", folder: "mlops-zoomcamp" },
  "sma-zoomcamp" => { repo: "DataTalksClub/stock-markets-analytics-zoomcamp", folder: "sma-zoomcamp" }
}.freeze

options = { date: Date.today, since: nil, out: nil, events_file: nil, luma: true }
OptionParser.new do |opts|
  opts.on("--date DATE", "Send date, YYYY-MM-DD (default: today)") { |v| options[:date] = Date.parse(v) }
  opts.on("--since DATE", "Start of the 'new this week' window (default: send date minus 7 days)") { |v| options[:since] = Date.parse(v) }
  opts.on("--out PATH", "Write the report to this file instead of stdout") { |v| options[:out] = v }
  opts.on("--events-file PATH", "Read events.yaml from a local file instead of GitHub") { |v| options[:events_file] = v }
  opts.on("--no-luma", "Skip checking event times on Luma") { options[:luma] = false }
end.parse!

send_date = options[:date]
since = options[:since] || (send_date - 7)
$warnings = []

def fetch(url)
  uri = URI(url)
  5.times do
    response = Net::HTTP.get_response(uri)
    return response.body.force_encoding(Encoding::UTF_8) if response.is_a?(Net::HTTPSuccess)
    raise "#{response.code} from #{uri}" unless response.is_a?(Net::HTTPRedirection)

    uri = URI.join(uri.to_s, response["location"])
  end
  raise "too many redirects for #{url}"
end

def try_fetch(url, what)
  fetch(url)
rescue StandardError => e
  $warnings << "Could not fetch #{what} (#{url}): #{e.message}"
  nil
end

def local(time)
  previous = ENV["TZ"]
  ENV["TZ"] = DISPLAY_TZ
  time.getlocal
ensure
  ENV["TZ"] = previous
end

# "September 29, 2026 at 01:00 CEST (September 28 at 23:00 UTC)"
def deadline_text(utc)
  l = local(utc)
  "#{l.strftime('%B %-d, %Y at %H:%M')} #{l.zone} (#{utc.strftime('%B %-d at %H:%M')} UTC)"
end

# "September 14, 12:30 PM CEST", dropping ":00" as the newsletter does ("5 PM")
def event_time_text(utc)
  l = local(utc)
  clock = l.min.zero? ? l.strftime("%-l %p") : l.strftime("%-l:%M %p")
  "#{l.strftime('%B %-d')}, #{clock} #{l.zone}"
end

# YAML reads naive timestamps such as "2026-09-18 23:59:59" as UTC; keep that date.
def to_date(value)
  return value.utc.to_date if value.is_a?(Time)
  return value if value.is_a?(Date)

  Date.parse(value.to_s)
rescue StandardError
  nil
end

def section(title, lines)
  ["## #{title}", "", *lines, ""]
end

def strip_tags(html)
  CGI.unescapeHTML(html.gsub(/<[^>]+>/, " ")).gsub(/\s+/, " ").strip
end

def front_matter(markdown)
  yaml = markdown.to_s[/\A---\s*\n(.*?)\n---/m, 1]
  yaml ? (YAML.safe_load(yaml, permitted_classes: [Date, Time]) || {}) : {}
rescue StandardError
  {}
end

$people = {}
def person_name(id)
  $people[id] ||= begin
    front_matter(fetch("#{SITE_RAW}/_people/#{id}.md"))["title"] || id
  rescue StandardError
    id
  end
end

# --- Zoomcamps (course platform) ----------------------------------------------

# Each course publishes every deadline (homework, project submission, peer
# review) with its link in a public calendar feed.
def calendar_items(ics)
  unfolded = ics.gsub(/\r?\n[ \t]/, "")
  unfolded.scan(/BEGIN:VEVENT(.*?)END:VEVENT/m).map(&:first).filter_map do |event|
    field = ->(name) { event[/^#{name}[^:\n]*:(.*)$/, 1].to_s.strip.gsub(/\\([,;\\])/, '\\1').gsub("\\n", " ") }
    summary, start = field.call("SUMMARY"), field.call("DTSTART")
    next if summary.empty? || start.empty?

    course, item = summary.split(": ", 2)
    item = item.to_s.sub(/ deadline\z/, "")
    kind = if item.end_with?(" peer review") then :peer_review
           elsif item.start_with?("Homework") then :homework
           else :project
           end
    { course: course, title: item.sub(/ (submission|peer review)\z/, ""), kind: kind,
      due: Time.parse(start).utc, url: field.call("URL") }
  end
end

def module_folders(repo)
  JSON.parse(fetch("https://api.github.com/repos/#{repo}/contents/"))
      .select { |item| item["type"] == "dir" && item["name"] =~ /\A\d{2}-/ }
      .to_h { |item| [item["name"][0, 2].to_i, item["html_url"]] }
rescue StandardError => e
  $warnings << "Could not list module folders in #{repo}: #{e.message}"
  {}
end

def telegram_announcement(folder, year, number)
  dirs = [File.join(ROOT, "courses", "campaigns", "#{folder}-#{year}", "copy-bank", "telegram"),
          File.join(ROOT, "courses", folder, "copy-bank", "telegram")]
  path = dirs.lazy.map { |dir| Dir[File.join(dir, "*module-#{number}-announcement.md")].first }.find(&:itself)
  path&.sub("#{ROOT}/", "")
end

zoomcamp_lines = []
home = try_fetch("#{PLATFORM}/", "course platform home page")
slugs = home.to_s.scan(%r{href="/([a-z0-9-]+)-(\d{4})/"}).uniq
latest = slugs.group_by(&:first).transform_values { |pairs| pairs.map { |_, y| y.to_i }.max }
latest.sort.each do |prefix, year|
  slug = "#{prefix}-#{year}"
  ics = try_fetch("#{PLATFORM}/#{slug}/calendar.ics", "calendar for #{slug}")
  next unless ics

  items = calendar_items(ics)
  next unless items.any? { |i| i[:due].to_date >= send_date - 7 && i[:due].to_date <= send_date + 28 }

  name = items.first[:course] || slug
  config = COURSES[prefix] || {}
  homeworks = items.select { |i| i[:kind] == :homework }.sort_by { |i| i[:due] }
  projects = items.reject { |i| i[:kind] == :homework }.sort_by { |i| i[:due] }

  zoomcamp_lines << "### #{name}"
  zoomcamp_lines << ""
  zoomcamp_lines << "- Platform: #{PLATFORM}/#{slug}/"

  # A deadline on the send day or the day after closes last week's module;
  # the module readers start this week is the next homework after that.
  homeworks.select { |h| h[:due].to_date >= send_date && h[:due].to_date < send_date + 2 }.each do |h|
    zoomcamp_lines << "- Closing now (last week's module): #{h[:title]}, due #{deadline_text(h[:due])}"
  end
  next_hw = homeworks.find { |h| h[:due].to_date >= send_date + 2 }
  if next_hw.nil? && homeworks.any? && projects.none? { |p| p[:due].to_date >= send_date }
    zoomcamp_lines << "- No homework or project due after the send date."
  elsif next_hw
    days = (next_hw[:due].to_date - send_date).to_i
    number = next_hw[:title][/Homework (\d+)/, 1].to_i
    zoomcamp_lines << "- This week's module: #{next_hw[:title]}, due #{deadline_text(next_hw[:due])} (#{days} days after send)"
    zoomcamp_lines << "  - Homework page: #{next_hw[:url]}" if next_hw[:url]
    if config[:repo]
      folder_url = module_folders(config[:repo])[number]
      zoomcamp_lines << "  - Module materials: #{folder_url || "TODO(no #{format('%02d', number)}- folder in #{config[:repo]})"}"
    end
    announcement = config[:folder] && telegram_announcement(config[:folder], year, number)
    zoomcamp_lines << "  - Module announcement to condense: `#{announcement}`" if announcement
  else
    zoomcamp_lines << "- No homework due after the send date. If modules remain, the next homework may not be on the platform yet."
  end

  projects.select { |p| p[:due].to_date >= send_date && p[:due].to_date <= send_date + 21 }.each do |p|
    if p[:kind] == :peer_review
      zoomcamp_lines << "- Peer review open: #{p[:title]}, reviews due #{deadline_text(p[:due])}"
      zoomcamp_lines << "  - Review page for learners: #{p[:url]}/eval"
    else
      zoomcamp_lines << "- Project submission: #{p[:title]}, due #{deadline_text(p[:due])}"
      zoomcamp_lines << "  - Project page: #{p[:url]}"
    end
  end
  zoomcamp_lines << ""
end
zoomcamp_lines = ["No course on #{PLATFORM} has a deadline between #{send_date - 7} and #{send_date + 28}."] if zoomcamp_lines.empty?

# --- Events and recordings ---------------------------------------------------

events = begin
  raw = options[:events_file] ? File.read(options[:events_file]) : fetch("#{SITE_RAW}/_data/events.yaml")
  YAML.safe_load(raw, permitted_classes: [Date, Time]) || []
rescue StandardError => e
  $warnings << "Could not load events.yaml: #{e.message}"
  []
end

def event_date(event)
  to_date(event["time"])
end

def speakers(event)
  names = Array(event["speakers"]).map { |id| person_name(id) }
  names.empty? ? nil : "speakers: #{names.join(', ')}"
end

upcoming = events.select { |e| (d = event_date(e)) && d >= send_date }.sort_by { |e| e["time"].to_s }
event_lines = upcoming.map do |e|
  start = nil
  if options[:luma] && e["link"].to_s.include?("luma.com")
    html = try_fetch(e["link"], "Luma page")
    start_at = html.to_s[/"start_at":"([^"]+)"/, 1]
    start = Time.parse(start_at).utc if start_at
  end
  when_text = start ? event_time_text(start) : "#{e['time'].is_a?(Time) ? e['time'].utc.strftime('%Y-%m-%d %H:%M') : e['time']} (from events.yaml, not verified on Luma)"
  details = ["link: #{e['link']}", speakers(e)].compact
  "- #{when_text} | #{e['type'].to_s.capitalize}: #{e['title']}\n  - #{details.join('; ')}"
end
event_lines = ["No upcoming events in events.yaml."] if event_lines.empty?

recordings = events.select { |e| (d = event_date(e)) && d >= since && d < send_date && e["youtube"] }
                   .sort_by { |e| e["time"].to_s }.reverse
recording_lines = recordings.map do |e|
  details = ["recording: #{e['youtube']}", "event page: #{e['link']}", speakers(e)].compact
  "- #{event_date(e)} | #{e['type'].to_s.capitalize}: #{e['title']}\n  - #{details.join('; ')}"
end
recording_lines = ["No events with a recording between #{since} and #{send_date - 1}."] if recording_lines.empty?

# --- Book of the Week --------------------------------------------------------

book_lines = begin
  files = JSON.parse(fetch("#{SITE_API}/contents/_books")).map { |f| f["name"] }
  week = (send_date..send_date + 6)
  candidates = files.select { |f| (d = (Date.strptime(f[0, 8], "%Y%m%d") rescue nil)) && d >= send_date - 7 && d <= send_date + 7 }
  books = candidates.filter_map do |file|
    meta = front_matter(fetch("#{SITE_RAW}/_books/#{file}"))
    start = to_date(meta["start"])
    finish = to_date(meta["end"])
    next unless start && finish && start <= week.last && finish >= week.first

    authors = Array(meta["authors"]).map { |id| person_name(id) }.join(", ")
    "- #{meta['title']} by #{authors}, #{start.strftime('%B %-d')}–#{finish.strftime('%B %-d')}\n" \
      "  - Participate link: https://datatalks.club/books/#{File.basename(file, '.md')}.html\n" \
      "  - Description: #{SITE_RAW}/_books/#{file}"
  end
  books.empty? ? ["No Book of the Week runs between #{week.first} and #{week.last}."] : books
rescue StandardError => e
  $warnings << "Could not read books from the website repo: #{e.message}"
  ["Unknown: books unavailable."]
end

# --- Alexey on Data ----------------------------------------------------------

def cdata(text)
  CGI.unescapeHTML(text.to_s.sub(/\A\s*<!\[CDATA\[/, "").sub(/\]\]>\s*\z/, "").strip)
end

post_lines = begin
  feed = fetch(FEED_URL)
  items = feed.scan(%r{<item>(.*?)</item>}m).map(&:first).map do |item|
    {
      title: cdata(item[%r{<title>(.*?)</title>}m, 1]),
      link: cdata(item[%r{<link>(.*?)</link>}m, 1]),
      summary: cdata(item[%r{<description>(.*?)</description>}m, 1]),
      date: (Time.parse(item[%r{<pubDate>(.*?)</pubDate>}m, 1]).utc.to_date rescue nil)
    }
  end
  fresh = items.select { |i| i[:date] && i[:date] >= since && i[:date] < send_date }
  if fresh.empty?
    latest_post = items.first
    ["No new posts between #{since} and #{send_date - 1}.",
     (latest_post ? "Latest post: #{latest_post[:date]} | #{latest_post[:title]} | #{latest_post[:link]}" : nil)].compact
  else
    fresh.map { |i| "- #{i[:date]} | #{i[:title]}\n  - #{i[:link]}\n  - #{i[:summary]}" }
  end
rescue StandardError => e
  $warnings << "Could not read #{FEED_URL}: #{e.message}"
  ["Feed unavailable."]
end

# --- Issue number ------------------------------------------------------------

numbers = Dir[File.join(ROOT, "newsletter", "issues", "*")].map { |p| File.basename(p)[/weekly-(\d+)/, 1] }.compact.map(&:to_i)
issue_line = numbers.empty? ? "Unknown: no past issues in newsletter/issues/." : "#{numbers.max + 1} (last saved issue is ##{numbers.max})"

# --- Report ------------------------------------------------------------------

report = [
  "# Sources for DataTalks.Club Weekly, #{send_date.strftime('%B %-d, %Y')}",
  "",
  "Generated #{Time.now.utc.strftime('%Y-%m-%d %H:%M')} UTC. 'New this week' window: #{since} to #{send_date - 1}.",
  "",
  *section("Issue number", [issue_line]),
  *section("Running Zoomcamps", zoomcamp_lines),
  *section("Upcoming events", event_lines),
  *section("Book of the Week", book_lines),
  *section("New recordings", recording_lines),
  *section("Alexey on Data", post_lines),
  *($warnings.empty? ? [] : section("Warnings", $warnings.map { |w| "- #{w}" }))
].join("\n")

if options[:out]
  File.write(options[:out], report)
  puts "Wrote #{options[:out]}"
else
  puts report
end
