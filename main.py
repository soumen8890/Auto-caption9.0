import os
import threading
from pyrogram import Client
from Info import Info
import handlers.caption
import handlers.buttons
import server

def run_bot():
    app = Client(
        "AutoCaptionBot",
        api_id=Info.API_ID,
        api_hash=Info.API_HASH,
        bot_token=Info.BOT_TOKEN
    )
    app.run()

def run_server():
    server.app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

if __name__ == "__main__":
    p1 = Process(target=run_bot)
    p2 = Process(target=run_server)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
