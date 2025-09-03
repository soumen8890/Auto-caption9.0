from pyrogram import Client, filters
from utils.metadata import extract_info
from database import captions

@Client.on_message(filters.document | filters.video | filters.audio)
async def auto_caption(client, message):
    file = message.document or message.video or message.audio
    filepath = await message.download()
    meta = extract_info(filepath)

    caption_text = f"""
📁 File: {meta.get('filename')}
📦 Size: {file.file_size // (1024*1024)} MB
🖼 Resolution: {meta.get('resolution')}
⏱ Duration: {meta.get('duration')}
🎶 Artist: {meta.get('artist')}
🎵 Title: {meta.get('title')}
"""

    # Save caption in DB
    captions.insert_one({"file_id": file.file_unique_id, "caption": caption_text})

    await message.reply_text(caption_text)
