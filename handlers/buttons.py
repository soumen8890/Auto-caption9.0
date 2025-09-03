from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Info import Info
from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("👋 Hello! I am alive.")

@Client.on_message(filters.command("setbutton") & filters.user(Info.OWNER_ID))
async def set_button(client, message):
    text = "Click below 👇"
    buttons = [[InlineKeyboardButton("My Channel", url="https://t.me/yourchannel")]]
    await message.reply("✅ Button Set!", reply_markup=InlineKeyboardMarkup(buttons))
