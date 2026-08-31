#!/usr/bin/env ruby

require "date"
require "json"
require "yaml"

ROOT = File.expand_path("..", __dir__)
SCHEMA_PATH = File.join(ROOT, "courses", "schema", "course.schema.json")

schema = JSON.parse(File.read(SCHEMA_PATH))
required_top_level = schema.fetch("required")
required_course = schema.dig("properties", "course", "required")
required_urls = schema.dig("properties", "urls", "required")
required_delivery = schema.dig("properties", "delivery", "required")

paths = if ARGV.empty?
  Dir[File.join(ROOT, "courses", "*", "course.yaml")] +
    Dir[File.join(ROOT, "courses", "campaigns", "*", "course.yaml")]
else
  ARGV.map { |path| File.expand_path(path, Dir.pwd) }
end

errors = []

def require_keys(errors, path, label, value, keys)
  unless value.is_a?(Hash)
    errors << "#{path}: #{label} must be an object"
    return
  end

  keys.each do |key|
    errors << "#{path}: missing #{label}.#{key}" unless value.key?(key)
  end
end

paths.uniq.sort.each do |path|
  begin
    data = YAML.safe_load(File.read(path), aliases: true)
  rescue Psych::SyntaxError => e
    errors << "#{path}: invalid YAML: #{e.message.lines.first.strip}"
    next
  end

  unless data.is_a?(Hash)
    errors << "#{path}: root must be an object"
    next
  end

  require_keys(errors, path, "root", data, required_top_level)
  require_keys(errors, path, "course", data["course"], required_course)
  require_keys(errors, path, "urls", data["urls"], required_urls)
  require_keys(errors, path, "delivery", data["delivery"], required_delivery)

  %w[community_and_support instructors].each do |legacy_key|
    errors << "#{path}: use canonical key instead of #{legacy_key}" if data.key?(legacy_key)
  end

  %w[topics tools modules].each do |key|
    value = data[key]
    errors << "#{path}: #{key} must be a non-empty array" unless value.is_a?(Array) && !value.empty?
  end

  community = data["community"]
  if community.is_a?(Hash)
    has_support = community.key?("support_channels") || community.key?("primary_support_channel")
    errors << "#{path}: community needs support_channels or primary_support_channel" unless has_support
  end

  people = data["people"]
  if people && (!people.is_a?(Hash) || !people["instructors"].is_a?(Array))
    errors << "#{path}: people.instructors must be an array"
  end

  researched_on = data.dig("research_metadata", "researched_on")
  begin
    Date.iso8601(researched_on.to_s)
  rescue Date::Error
    errors << "#{path}: research_metadata.researched_on must be YYYY-MM-DD"
  end

  slug = data.dig("course", "slug")
  unless slug.is_a?(String) && slug.match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\z/)
    errors << "#{path}: course.slug must use lowercase kebab-case"
  end
end

if errors.empty?
  puts "Validated #{paths.uniq.length} course files against #{SCHEMA_PATH.sub(ROOT + "/", "")}."
  exit 0
end

warn errors.join("\n")
exit 1
