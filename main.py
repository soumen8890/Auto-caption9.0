from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("👋 Hello! Your bot is working fine now.")

@app.on_message(filters.text & ~filters.command("start"))
async def echo_handler(client, message):
    await message.reply_text(f"You said: {message.text}")

print("🤖 Bot started...")
app.run()
