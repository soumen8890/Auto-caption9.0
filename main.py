import os
import threading
from pyrogram import Client
from Info import Info
import handlers.caption
import handlers.buttons
import server
import logging
logging.basicConfig(level=logging.INFO)

def run_bot():
    app = Client(
        "AutoCaptionBot",
        api_id=Info.API_ID,
        api_hash=Info.API_HASH,
        bot_token=Info.BOT_TOKEN
    )
    print("✅ Telegram bot is starting...")
    app.run()

def run_server():
    port = int(os.environ.get("PORT", 10000))
    print(f"✅ Web server running on port {port}")
    server.app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    t1 = threading.Thread(target=run_bot)
    t2 = threading.Thread(target=run_server)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
