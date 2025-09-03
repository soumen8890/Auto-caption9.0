from pyrogram import Client
from Info import Info
import handlers.caption
import handlers.buttons

app = Client(
    "AutoCaptionBot",
    api_id=Info.API_ID,
    api_hash=Info.API_HASH,
    bot_token=Info.BOT_TOKEN
)

app.run()
