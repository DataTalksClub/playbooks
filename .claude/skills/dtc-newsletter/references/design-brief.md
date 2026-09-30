# Design Brief

This brief covers the design of DataTalks.Club Weekly: the images to create (Part A) and how to set up the Mailchimp template (Part B). It is for whoever designs the images and whoever rebuilds or fills in the template. What goes into each slot is in `slots.md` and `issue-structure.md`.

Each Part B section gives the spec first. It then lists **Fix in the current template**: the differences found in a review of the #296 template on 2026-09-28. Delete a fix line once it is done.

## Goals

- Readers recognize the newsletter and each section after one second of scrolling.
- Sponsored content is clearly separate from editorial content and looks good enough that future sponsors trust the placement when they review past issues.
- The email looks finished in every major client, including with images off and in dark mode.
- The HTML stays under Gmail's 102 KB clipping limit.

## Status

| Piece | Status |
| --- | --- |
| A1 Masthead logo | Done |
| A2 Course banners | Machine Learning Zoomcamp needs resizing. The other four are still to make. |
| B1 Global styles | Link color and blue buttons done. Button text and the Events section styles need fixing. |
| B2 Top bar and masthead | Top bar done. The masthead line and "This week" need fixing. |
| B3 Section labels and dividers | Labels in place. Spacing and divider colors need fixing. |
| B4 Sponsor block | Tint and label done. Block order needs fixing. |
| B5 Course slots | Heading size and an extra divider need fixing. |
| B6 Events | Row layout in place. Link styles, divider color, and alignment need fixing. |
| B7 Recordings and Read | Needs rebuilding. |
| B8 Footer | Not started. |

## Quick Reference

| What | Value |
| --- | --- |
| Email width | 660 px, with 24 px side padding, so content is 612 px wide |
| Full-width image | Export 1224 px wide (2x) and display at 612 px. Images already exported at 1200 px are fine. |
| Accent blue: buttons, links, section labels | `#2056A2` |
| Body text | `#222222` on `#FFFFFF` |
| Muted grey: top bar, masthead line, footer | `#656565` |
| Divider line | 1 px solid `#E5E5E5` |
| Light tint: sponsor block, course banner background | `#EEF0F7` (the current sponsor block). Check it against the Machine Learning Zoomcamp banner background; if they differ, pick one and use it in both. |
| Font in images | Ubuntu Bold |
| Font in live text | Helvetica Neue, Helvetica, Arial, sans-serif |

| Element | Style |
| --- | --- |
| Slot heading | Heading 2: bold, 24 px, `#222222` |
| Body | 16 px, line height 1.5 |
| Section label | 13 px bold capitals, 1.5 px letter spacing, accent blue (B3) |
| Event date line | Bold, body size |
| Masthead line and footer | 14 px, muted grey |

## Rules For Every Piece

- **Never put information only in an image.** Some clients block images by default (Outlook desktop and many work accounts), and screen readers skip them. Every image gets alt text, and anything the reader needs, such as a course name or date, also appears as live text or in the alt text.
- **Image files:** PNG for text or flat color, JPG for photos, each under 200 KB.
- **Web fonts:** Most email clients ignore them. Use Ubuntu Bold only inside images.
- **Dark mode:** Apple Mail, Gmail, and Outlook may invert light backgrounds. Give logos a transparent background, or a solid background that still looks intentional on a dark page.
- **Size:** Every Mailchimp block adds about 8 KB of HTML. Images do not count toward the 102 KB limit. Use as few blocks as possible and put a whole section in one text block where the block map (Part B) allows it. Layout (column) blocks are the most expensive: use them only for the Upcoming events rows (B6).
- **Styles:** Do not set text colors or fonts per section or per link. Everything uses the template's global styles (B1).

## Part A: Images To Create

| # | Piece | Export / display size | Content | Alt text | Status |
| --- | --- | --- | --- | --- | --- |
| A1 | Masthead logo lockup | 1224 × 200 / 612 × 100 | The DataTalks.Club logo and the words "DataTalks.Club Weekly". No issue number or date: these change weekly and stay as live text. | `DataTalks.Club Weekly` | Done (2026-09-25): the DataTalks.Club speech-bubble logo, "DataTalks.Club" in blue, "Weekly" in black |
| A2 | Course banner, one per course | 1224 × 160 / 612 × 80 | A colored square with the course initials on the left. On the right, on one line, the "DATATALKS.CLUB · FREE COURSE" label and the course name. Tint background. | The course name, for example `Machine Learning Zoomcamp` | Machine Learning Zoomcamp exists at about 600 × 120 and needs shortening to 80 px high. The others are still to make. |
| A3 | Sponsor logo or banner, supplied by the sponsor | Logo: up to 612 × 160 / 306 × 80. Banner: 1224 / 612 wide. | The sponsor's own logo or event banner, used only when the sponsor sends one | What the image says, for example `Webinar: Best practices for ETL in 2026, October 15` | Per issue |

Course banners are needed for these course folders in `courses/`: AI Dev Tools Zoomcamp, Data Engineering Zoomcamp, LLM Zoomcamp, Machine Learning Zoomcamp, and MLOps Zoomcamp. Keep one template, so a new course only needs new initials and a new name. AI Engineering Buildcamp is a paid product that runs in the promo slot, so it uses the sponsor block, not a course banner.

**Not planned:** recording thumbnails, event posters, and decorative images. They make the email longer without adding information. If recording clicks stay low, test a single thumbnail on the workshop recording later.

## Part B: Mailchimp Template

The template is built in Mailchimp's new email builder. Sections have their own background setting, and each block has its own style settings. Build everything below as native blocks, not images, so it works with images off and is easy to edit each week.

### Block Map

This is the whole email from top to bottom. Every other section of this brief expands one row of it. "Fixed" means set once in the template; "weekly" means filled in from `issue.md` for each issue.

| # | Part | Blocks | Filled |
| --- | --- | --- | --- |
| 1 | Top bar (B2) | Text | Fixed |
| 2 | Masthead (B2) | Image (A1), then one text block: the masthead line and "This week" | Weekly text |
| 3 | Masthead divider (B3) | Divider | Fixed |
| 4 | Sponsor (B4), only when an issue has one | Text block with the `SPONSORED` label on white, then a tinted section: image (A3, optional), text, button | Weekly |
| 5 | Course slots (B5), one per course | Image (A2), text, button | Weekly |
| 6 | Events (B6) | Divider, text (label and detail slot), button (optional), one two-column row per upcoming event, text (calendar links) | Weekly |
| 7 | Recordings (B7) | Divider, one text block | Weekly |
| 8 | Read (B7) | Divider, one text block | Weekly |
| 9 | Footer (B8) | Text and social icons | Fixed |

Delete the rows the issue does not use, together with their label and divider. Never send an empty label.

A secondary promo uses a copy of row 4, placed after the course slots. It has a divider above its label.

### B1. Global Styles

Set these once in the template's global styles. Leave every section and block on the defaults.

- **Text:** `#222222`, 16 px, line height 1.5. Slot headings are Heading 2 (24 px bold).
- **Links:** accent blue `#2056A2`, underlined.
- **Buttons:** one style everywhere. Accent blue background, white bold text, 8 px corner radius, 16 px × 28 px padding, centered. Use buttons only for the sponsor, course, and event detail slots. Recordings and Read use text links (B7).

**Fix in the current template:**

- The Events section overrides paragraph text to `#8C8C8C` (too light to read, 3.4:1 contrast) and links to black. Reset its text and link colors to the global defaults. In the HTML this is the `.mceSection84` rule.
- The button text is normal weight. Set it to bold.
- Remove the second button style: "View full calendar" (white with a black border). B6 replaces it with a text link.

### B2. Top Bar And Masthead

- **Top bar:** "View this email in your browser" (`*|ARCHIVE|*`) in 14 px muted grey, aligned right, above the logo. Done.
- **Logo:** the A1 image with alt text `DataTalks.Club Weekly`.
- **Masthead text block:** one text block directly under the logo, with two paragraphs:
  1. The masthead line, for example `#296 · September 28, 2026`: centered, 14 px, regular weight, muted grey. It identifies the issue and must not compete with the first heading.
  2. The **This week** summary from `issue.md`, in body style, aligned left.
- The masthead divider (B3) follows.

**Fix in the current template:**

- The issue number and date are in a two-column layout ("#296" on the left, the date on the right). On mobile they stack onto two lines, and the layout adds several KB. Replace it with the single centered masthead line in the masthead text block.
- The "This week" block starts with an empty `<p><br/></p>`. Delete it.
- The logo has `alt=""`. Set it to `DataTalks.Club Weekly`.

### B3. Section Labels And Dividers

A section label is a short word in small bold capitals with wide letter spacing, in the accent blue. It sits above the first heading of a section. It matches the "DATATALKS.CLUB · FREE COURSE" line on the course banners, so banners and labels read as one system.

Preview: `design/section-labels-preview.png` (source: `design/section-labels-preview.html`).

**Labels.** Use exactly these, in this order, and only for sections that are in the issue:

| Label | Covers |
| --- | --- |
| `SPONSORED` | Primary or secondary promo (B4) |
| `EVENTS` | Event detail slots and the Upcoming events list |
| `RECORDINGS` | Workshop, podcast, and webinar recordings |
| `READ` | Book of the Week and From Alexey on Data |

Courses get no label, because their banners mark them.

**Label.** The label is the first line of the section's text block. Paste it in the block's source code view:

```html
<p style="margin:0 0 12px;font-family:Helvetica,Arial,sans-serif;font-size:13px;line-height:18px;font-weight:bold;letter-spacing:1.5px;color:#2056A2;">EVENTS</p>
```

Type the label in capitals; do not rely on CSS uppercase, which some clients ignore. The 12 px bottom margin is the gap to the heading. Do not put the label in a block of its own: two blocks of padding double that gap. The only exception is the `SPONSORED` label, which sits on white above the tinted block (B4).

**Divider.** A Divider block with a 1 px solid `#E5E5E5` line across the full content width, 40 px of padding above, and 24 px below. Dividers go in two places only:

- after the masthead (fixed in the template);
- above every section label after that, except `SPONSORED` directly after the masthead, which already has the masthead divider above it.

The only other dividers are the lines between Upcoming events rows (B6). There is never a divider between slots inside a section, and never one above a course banner. Use 32 px of white space there instead. Inside a text block, add it to every slot heading after the first one:

```html
<h2 style="margin-top:32px;">Podcast recording: Decoding the Open Lakehouse</h2>
```

**Fix in the current template:**

- Every divider has 12 px of padding above and below. Set it to 40 px above and 24 px below.
- The dividers between Upcoming events rows are black (`#000000`). Set them to `#E5E5E5` (B6).
- The `EVENTS`, `RECORDINGS`, and `READ` labels are in blocks of their own and lack the 18 px line height. Move each label into its section's text block using the snippet above.
- A divider sits above the course banner. Remove it.

### B4. Sponsor Block

- The `SPONSORED` label goes above the block, on the white background, outside the tint. It uses the B3 style. It can link to the page about sponsoring the newsletter. The template's link style would remove the bold and add an underline, so repeat every text style on the link itself:
  ```html
  <p style="margin:0 0 12px;font-family:Helvetica,Arial,sans-serif;font-size:13px;line-height:18px;font-weight:bold;letter-spacing:1.5px;color:#2056A2;"><a href="https://..." style="font-family:Helvetica,Arial,sans-serif;font-size:13px;font-weight:bold;letter-spacing:1.5px;color:#2056A2;text-decoration:none;">SPONSORED</a></p>
  ```
- The block is a section with the tint background `#EEF0F7` and the same padding on every side.
- Inside the block, in this order: the sponsor image (A3, only if supplied), a text block with the heading and body, then the button. The image comes first because it draws the eye; the heading and body carry the offer in live text for readers with images off.
- Link the sponsor image to the same URL as the button, including the sponsor's tracking parameters. Sponsor banners often show their own button, such as "Attend", and readers click it.

**Fix in the current template:**

- The heading comes before the image. Move the image to the top.
- The image is not linked. Link it to the button URL each week.

### B5. Course Slots

One slot per course, in the order from `issue-structure.md`:

1. The course banner (A2), with the course name as alt text. Without a banner, skip the image and use the fallback heading from `issue-structure.md`.
2. A text block: the slot heading as Heading 2 (`Module N: [module title]`), then the body.
3. A `Join Module N` button.

Between two course slots, leave 32 px of white space. Do not add a divider.

**Fix in the current template:**

- The course heading is Heading 3 (20 px). Change it to Heading 2, like every other slot heading.
- The banner has `alt=""`. Set the course name each week.

### B6. Events

1. A divider.
2. A text block: the `EVENTS` label, then the event detail slot's heading and body, if there is one.
3. The detail slot's button, if it has one. A course event series has no button.
4. The Upcoming events list: the `Upcoming events` heading (only when a detail slot comes before it), then one row per event, then a closing links line.

The Upcoming events list is the visual centerpiece of the section, not a plain list. Each event is a two-column row (a Layout block), so the date reads at a glance:

| Left column (5 of 12) | Right column (7 of 12) |
| --- | --- |
| **Tue, September 29** in bold, `#222222` | **Event title** as a link in the accent blue |
| 5:30 PM CEST, regular | `Webinar with Suhas Suresha` in body text |

- The `issue.md` entry maps onto the row: its bold date line goes in the left column (date on the first line, time on the second), and its title link and "Webinar with…" line go in the right column.
- Separate rows with a 1 px `#E5E5E5` divider, the same as the section dividers.
- Line up the date column's text with the 24 px gutter that the rest of the email uses, on desktop and on mobile.
- On mobile the columns stack: the date sits above the title. Check this in a test send.
- End with one text block: `See all upcoming events · Add our events to your calendar`, both text links, in the format from `slots.md`.

**Size.** The Layout rows are the one exception to "no layout blocks" in Rules For Every Piece. Each row adds about 5 KB, so budget for them: list at most five events and let the calendar link cover the rest. If a test send shows "[Message clipped]", merge blocks in the Recordings and Read sections first, before touching the events rows.

**Fix in the current template:**

- The event links carry styles pasted from VS Code: `color: rgb(0,106,177)`, a system font stack, and 14 px. Remove them so the links use the global link style (see Weekly Build Checklist).
- The dividers between rows are black (`#000000`). Set them to `#E5E5E5`.
- The date column is indented 40 px and the title column 30 px, and on mobile the indents change again (30 px). Align both with the 24 px gutter.
- The three rows are copies of the same event. The rows must follow `issue.md`.
- The "View full calendar" button becomes the text link line above. The calendar link was missing.
- Delete the placeholder image in the detail slot (no event posters).
- Decide what the rounded, black-bordered image under the "Upcoming events" heading is for. If it stays, give it alt text; if it carries no information, remove it.

### B7. Recordings And Read

Each section is one divider and one text block:

- the label;
- each slot's heading (Heading 2) and body;
- the slot's link on its own line, as a text link rather than a button: `Watch the recording →`, `Participate here →`, `Read here →`.

Recordings go in the order workshop, podcast, webinar. Leave 32 px above every heading after the first one (B3).

Drop a section, including its label and divider, when it has no slots. #296 has no Read section, for example.

**Fix in the current template:**

- Delete the three video placeholder images (no recording thumbnails).
- The order is workshop, webinar, podcast. Change it to workshop, podcast, webinar.
- Recordings have no link. Add the text link under each one.
- Merge the separate heading and description blocks into one text block per section.
- The `READ` label has nothing under it. Keep it in the template only as a starting point and delete it in issues without Read slots.

### B8. Footer

Keep, from the old footer:

- The Slack invite paragraph. Capitalize "Slack" in "join our slack".
- The invite-problems form link and the "Hit reply" line.
- The "Thanks for reading! This newsletter was written by…" signature, as plain text or on a light background. The old dark block was the heaviest element in the email.

Add:

- A links row: `Forward to a friend` (`*|FORWARD|*`) · `Subscribe` (`*|LIST:SUBSCRIBE|*`) · `Past issues` (TODO: archive URL) · `Sponsor this newsletter` (TODO: sponsorship URL. The `SPONSORED` label currently links to `https://datatalks.club/support`; if that is the sponsorship page, use it here too). The sponsor line can carry one sentence about the audience (TODO: the audience size to quote).
- Social icons for X, LinkedIn, YouTube, and the website. Add Telegram if DataTalks.Club promotes its Telegram channel.

Mailchimp's required parts are already in the template: the copyright line, the postal address (`*|HTML:LIST_ADDRESS|*`, hidden on the archive page), and the update preferences and unsubscribe links. Keep them.

**Fix in the current template:**

- Only Mailchimp's default footer is there. Add everything in the lists above.
- The footer text is 12 px italic. Set it to 14 px regular, muted grey.

## Weekly Build Checklist

Use this when filling the template from `issue.md`:

1. **Paste as plain text** (Cmd+Shift+V on Mac, Ctrl+Shift+V on Windows). Copying from a Markdown preview, such as VS Code, carries its fonts and colors into Mailchimp. If a link or paragraph looks different from the rest, open the source code view and remove any `style="..."` on `<a>` and `<span>` tags.
2. Update the masthead line and the **This week** summary.
3. Delete every block, label, and divider for sections not in the issue.
4. In each text block's source code view, delete empty `<p>` and `<br>` lines at the start and end.
5. Set alt text on every image: course names on banners, the sponsor image's text on the sponsor image.
6. Send a test to yourself and open it in Gmail. If you see "[Message clipped]", merge blocks until it goes away.

## Checks Before The First Send With The New Template

Send tests to yourself, not to the audience, and check:

- Gmail web and mobile: no "[Message clipped]" notice.
- Outlook desktop with images off: every section still makes sense from the live text and alt text.
- Apple Mail and Gmail in dark mode: the logo and banners stay readable.
- Every button and link uses the accent blue, and no text is light grey outside the top bar, masthead line, and footer.
- The sponsor block is clearly labeled at the top.
