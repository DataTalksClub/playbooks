"""Read-only identity and channel-admin check with a Dapier-injected token."""
import argparse
import json
import os
import sys
import urllib.request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chat", action="append", default=[], help="@channel or numeric chat ID")
    args = parser.parse_args()
    token = os.environ.get("DAPIER_ACCESS_TOKEN")
    if not token:
        parser.error("Run through dapier token exec; DAPIER_ACCESS_TOKEN is missing")

    def call(method, payload=None):
        request = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/{method}",
            data=json.dumps(payload or {}).encode(),
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                data = json.load(response)
        except Exception as exc:
            # URLs contain the secret. Never print an exception or traceback.
            raise RuntimeError(f"{method} failed ({type(exc).__name__})") from None
        if not data.get("ok"):
            raise RuntimeError(f"{method} rejected by Telegram")
        return data["result"]

    try:
        bot = call("getMe")
        result = {"bot_id": bot["id"], "username": bot.get("username"), "channels": []}
        failed = False
        for requested_chat in args.chat:
            channel = {"requested": requested_chat}
            try:
                chat = call("getChat", {"chat_id": requested_chat})
                channel.update({"chat_id": chat["id"], "title": chat.get("title"),
                                "username": chat.get("username"), "type": chat["type"]})
                member = call("getChatMember", {"chat_id": chat["id"], "user_id": bot["id"]})
                channel.update({"status": member["status"],
                                "can_post_messages": member.get("can_post_messages", False),
                                "can_edit_messages": member.get("can_edit_messages", False)})
                channel["ready_to_post"] = (chat["type"] == "channel"
                                            and member["status"] == "administrator"
                                            and channel["can_post_messages"])
                failed = failed or not channel["ready_to_post"]
            except RuntimeError as exc:
                channel.update({"ready_to_post": False, "error": str(exc)})
                failed = True
            result["channels"].append(channel)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return int(failed)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
