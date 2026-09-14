# idea_005: The best bug came from using the bot

Angle: A live Telegram test found an agent loop, and that failure should become a regression test or eval case.

Source moments:
- 01:52:46-01:56:38: The CLI agent is wrapped in Telegram and manually tested.
- 01:59:15-02:02:01: The bot keeps calling the same search tool, revealing the need for a tool-call limit and an assertion.

Post notes:
- Make the failure a positive engineering story.
- Mention monitoring because it made the loop visible.
- End with a concrete rule: when a demo finds a bug, encode it.
