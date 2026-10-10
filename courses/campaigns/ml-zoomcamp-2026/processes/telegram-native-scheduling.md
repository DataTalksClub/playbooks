# Schedule approved announcements in Telegram Web

Use Telegram Web A's native scheduled-message queue for the reviewed ML Zoomcamp 2026 announcements. Dapier stores credentials and supplies read-only platform facts. It does not schedule these posts. This guide describes the observed Web A controls; it is not evidence that any message has been queued.

The approved destination is ML Zoomcamp announcements, `@mlzoomcamp`, numeric channel ID `-1001435532197`. Use the [review plan](telegram-review-plan-2026-10-10.md) and approved message files. Record actual queue evidence in [the native execution ledger](telegram-native-execution-2026-10-11.json).

## Before scheduling

Refresh the course's live deadlines and states through the `course-telegram-management` skill's CMP helper. Compare recent channel posts and existing scheduled messages with the row's course/entity/kind and exact approved text hash. Confirm the old Dapier rule/workflow cannot also deliver this row.

Check the signed-in Telegram user's channel permissions and the browser/session timezone. The approved slot is 09:00 Europe/Berlin: 07:00 UTC before October 25, 2026, and 08:00 UTC from October 25 onward. If the scheduling UI uses another timezone, enter the local date and time representing the approved UTC instant. Do not apply a fixed offset to every row.

## Queue one message

1. Open the ML announcement channel and check its title and username. Open Scheduled Messages and check that the row is not already queued; return to the channel composer.
2. Paste the complete approved message as plain text in the composer. Check the opening, links, deadline, and ending against the source file. Preserve paragraph breaks; do not introduce formatting.
3. **Right-click Send Message.** A normal left-click sends immediately. Choose **Schedule Message** from the menu. Inside the already-open Scheduled Messages view, the composer?s send control opens the calendar directly; this was verified during migration. Check the scheduling view before using that shortcut.
4. Use the native calendar's month controls and day cell to select the intended date. Verify the month and year before choosing the day, particularly for the January 2027 rows. Adjacent-month days can repeat a number; choose the enabled current-month day and verify the final date label.
5. Set the two time text fields separately: **HH** and **MM**. For a Berlin-local 09:00 slot, enter `09` and `00`. Use the converted time when the UI timezone differs. Leave **Repeat** set to **Never**.
6. Inspect the scheduling dialog after setting the date and each time field. Verify the date, hour, minute, and final button label, such as **Send today at 09:00** or the chosen date at **09:00**. “Today” is correct only for a row scheduled on the current UI-local date.
7. Submit the schedule action once. Open or inspect **Scheduled Messages** and verify the resulting entry's date, time, and complete text in the correct channel. Count the new entry only after this check.
8. Record the row ID, file hash, planned UTC instant, actual UI timezone and displayed time, observed scheduled-message identifier if available, and verification evidence in the native execution ledger.

Read the rendered UI state after every action. Browser locators can intermittently fail; inspect the current dialog, composer, or queue before trying the next control. If the final schedule action times out or has an uncertain result, inspect Scheduled Messages before retrying. A retry can create a duplicate even when the first response failed.

## Verify and maintain the queue

Reconcile the complete scheduled-message queue against the approved rows. Check exact text and dates, not only the number of entries. A composer containing text, an open scheduling dialog, or a clicked button does not establish that a message is queued. Keep planned, verified queued, delivered, and uncertain statuses separate.

Native Telegram scheduling does not refresh CMP facts at delivery time. Review state-dependent reminders before release. Changed deadlines, unavailable materials, or a form in the wrong state require a manual edit or cancellation of the affected queued message and revised approval when content changes. After delivery, record the actual channel message ID/permalink and time when available.
