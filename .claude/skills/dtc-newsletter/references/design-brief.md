# Design Brief

This brief lists the design pieces DataTalks.Club Weekly needs: images to create, and parts to set up in the Mailchimp template. It is for whoever designs the images and whoever rebuilds the template. The slot content itself follows `slots.md` and `issue-structure.md`.

## Goals

- Readers recognize the newsletter and each section in a second of scrolling.
- Sponsored content is clearly separate from editorial content, and looks good enough that future sponsors reviewing past issues trust the placement.
- The email looks finished in every major client, including with images off and in dark mode.

## Email Constraints

These apply to every piece below.

- **Width.** The email body is 600 px wide. Export images at 2x (1200 px wide) so they stay sharp on high-density screens, and set them to display at 600 px.
- **Files.** PNG for images with text or flat color, JPG for photos. Keep each file under 200 KB.
- **Text in images.** Some clients block images by default (Outlook desktop, many work accounts), and screen readers skip them. Never put information only in an image: every image gets alt text, and anything the reader needs, such as a course name or date, also appears as live text nearby.
- **Fonts.** Most email clients ignore web fonts. Use Ubuntu Bold only inside images. Live text in the template uses Helvetica, Arial, sans-serif.
- **Dark mode.** Apple Mail, Gmail, and Outlook may invert light backgrounds. Give logos a transparent background, or a solid background that looks intentional when the surrounding page turns dark.
- **Size.** Gmail clips emails whose HTML is over 102 KB. Images do not count toward this limit, but every Mailchimp block adds about 8 KB of HTML. Prefer fewer, larger text blocks to many small ones (see `issue-structure.md`).

## Brand Values

| Token | Value | Source |
| --- | --- | --- |
| Accent blue | `#2056A2` | DataTalks.Club event poster Figma frame, recorded in `.claude/skills/video-clip-cutter/references/clip-styles.json` |
| Image font | Ubuntu Bold | Same source |
| Body text | `#222222` on `#FFFFFF` | Current template |
| Divider line | `#E5E5E5` | Chosen for this brief (B3) |
| Muted text (footer, top bar) | TODO: pick one grey and use it everywhere | |
| Light tint (sponsor block, banner background) | TODO: one light tint of the accent blue, sampled from the Machine Learning Zoomcamp banner | |

Use one blue for every button and every text link. The current template mixes a dark blue button, a light blue button, and teal links; replace all three with the accent blue.

## Part A: Images To Create

| # | Piece | Size (export / display) | Content | Alt text | Status |
| --- | --- | --- | --- | --- | --- |
| A1 | Masthead logo lockup | 1200 × 200 / 600 × 100 | DataTalks.Club logo and the words "DataTalks.Club Weekly". No issue number or date: those change weekly and stay as live text. | `DataTalks.Club Weekly` | To do |
| A2 | Course banners, one per course | 1200 × 160 / 600 × 80 | Colored square with the course initials on the left; "DATATALKS.CLUB · FREE COURSE" label and the course name on one line on the right; tint background. | The course name, for example `Machine Learning Zoomcamp` | Machine Learning Zoomcamp exists at about 600 × 120; shorten it to 600 × 80. Others to do. |
| A3 | Sponsor logo (supplied by the sponsor) | up to 600 × 160 / up to 300 × 80 | The sponsor's own logo, placed inside the sponsor block. Optional: use it only when the sponsor sends one. | The sponsor's name | Per issue |

Course banners needed, by course folder in `courses/`: AI Dev Tools Zoomcamp, Data Engineering Zoomcamp, LLM Zoomcamp, Machine Learning Zoomcamp, MLOps Zoomcamp. Keep one template so a new course only needs new initials and a name. AI Engineering Buildcamp is a paid product that runs in the promo slot, so it uses the sponsor block, not a course banner.

Course banners replace the course name in the slot heading. With a banner, the heading becomes `Module N: [module title]`, and the banner's alt text carries the course name for readers with images off.

Not planned for now: recording thumbnails and event posters. They make the email much longer. Test one for the workshop recording later if clicks on recordings stay low.

## Part B: Mailchimp Template Setup

Build these as native Mailchimp blocks and styles, not images, so they work with images off and are easy to edit each week.

### B1. Top bar

- A thin line above the masthead with "View in browser" (`*|ARCHIVE|*`) in small muted text, aligned right.
- Replaces the current large "View this email in your browser" link under the tagline.

### B2. Masthead

- The A1 logo image.
- One live text line under it: `#296 · September 28, 2026`. Updated each issue.
- A "This week" text block: one or two sentences naming the main items in the issue, written with each draft (rules in `issue-structure.md`, Output Format). It replaces the fixed tagline. If you keep the tagline, move it to the footer.

### B3. Section labels and dividers

A section label is a short word in small, bold, spaced-out capitals, in the accent blue, sitting above the first heading of a section. It matches the "DATATALKS.CLUB · FREE COURSE" line on the course banners, so banners and labels read as one system.

Preview: `design/section-labels-preview.png` (source: `design/section-labels-preview.html`). The tint in the preview's sponsor block is a placeholder.

**Labels.** Use exactly these, in this order, and only for sections present in the issue:

| Label | Covers |
| --- | --- |
| `SPONSORED` | Primary or secondary promo (see B4) |
| `EVENTS` | Event detail slots and the Upcoming events list |
| `RECORDINGS` | Workshop, podcast, and webinar recordings |
| `READ` | Book of the Week and From Alexey on Data |

Courses get no label: the course banners mark them.

**Label style.**

| Property | Value |
| --- | --- |
| Text | Typed in capital letters (do not rely on CSS uppercase, which some clients ignore) |
| Font | Helvetica, Arial, sans-serif, bold |
| Size | 13 px, line height 18 px |
| Letter spacing | 1.5 px. Mailchimp's style panel has no setting for it: set it in the text block's source code view (the snippet below). If Mailchimp strips it, wrap only the word in `<span style="letter-spacing:1.5px;">`. If that is stripped too, skip it: the label still works without it. |
| Color | Accent blue `#2056A2` |
| Space below | 12 px to the slot heading |

**Divider style.**

| Property | Value |
| --- | --- |
| Line | 1 px solid `#E5E5E5`, full content width |
| Space above | 40 px from the end of the previous section |
| Space below | 24 px to the section label |
| Where | Above every section label except the first one in the email. Never between slots inside a section; use 32 px of white space there instead. |

**Setting it up in Mailchimp.**

1. Where a section starts, add a Divider block. Set the border to 1 px solid `#E5E5E5`, top padding to 40 px, and bottom padding to 24 px.
2. Below it, use one Text block for the whole section. Open the block's source code view and paste the label as the first line:
   ```html
   <p style="margin:0 0 12px;font-family:Helvetica,Arial,sans-serif;font-size:13px;line-height:18px;font-weight:bold;letter-spacing:1.5px;color:#2056A2;">EVENTS</p>
   ```
3. Under the label, add each slot of the section with its own heading. Exception: when the Upcoming events list is the only thing under `EVENTS`, it goes directly under the label with no heading.

   Before saving, open the source code view and delete empty `<p>` or `<br>` lines before the label and after the last slot. They add the extra space that makes sections look loose. Build each section as one text block to keep the block count and HTML size down.
4. Once the dividers and labels are in the template, each week only the text under them changes.

### B4. Sponsor block

- A `SPONSORED` label above the block, not below it, in the same style as the other section labels (B3). It sits directly on the white background, outside the tinted block.
- The block has the light tint background and the same padding on all sides.
- Inside, in this order: optional sponsor logo (A3), heading, body, button.
- Drafts mark it with a `SPONSORED` line above the sponsor heading (see `issue-structure.md`, Output Format).

### B5. Buttons and links

- One button style everywhere: accent blue background, white bold text, rounded corners, generous padding, centered, full width on mobile.
- Text links in the accent blue, underlined.
- Use buttons for the main action of the sponsor and course slots. Lower slots, such as recordings and Book of the Week, may use a text link like `Watch the recording →` instead.

### B6. Type scale

| Element | Style |
| --- | --- |
| Slot heading | Bold, about 24 px |
| Body | 16 px, line height about 1.5 |
| Section label | 13 px bold capitals, 1.5 px letter spacing, accent blue (full spec in B3) |
| Event date line | Bold body size (format in `slots.md`, Upcoming Events) |
| Footer text | 14 px, muted |

### B7. Footer

Keep, with small fixes:

- The Slack invite paragraph. Capitalize "Slack" in "join our slack".
- The invite-problems form link and the "Hit reply" line.
- The "Thanks for reading! This newsletter was written by…" signature. Use a lighter background or plain text: the current dark block is the heaviest element in the email.

Add:

- A links row: `Forward to a friend` (`*|FORWARD|*`) · `Subscribe` (`*|LIST:SUBSCRIBE|*`) · `Past issues` (TODO: archive URL) · `Sponsor this newsletter` (TODO: sponsorship contact URL). The sponsor line can carry one sentence on the audience; TODO: the audience size to quote.
- A check of the social icons: X, LinkedIn, YouTube, website. Add Telegram if DataTalks.Club promotes its Telegram channel.
- The postal address. Mailchimp and anti-spam law require it, and the current footer screenshot does not show `*|LIST:ADDRESS|*`. Check in a test email whether Mailchimp adds it; if not, add the merge tag.

## Before The First Send With The New Template

Send tests to yourself (not to the audience) and check:

- Gmail web and mobile: no "[Message clipped]" notice.
- Outlook desktop with images off: every section still makes sense from live text and alt text.
- Apple Mail and Gmail in dark mode: the logo and banners stay readable.
- Every button and link uses the accent blue.
- The sponsor block is clearly labeled at the top.
