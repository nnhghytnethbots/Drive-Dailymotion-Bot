import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from downloader.drive import download_drive_file
from downloader.dailymotion import download_dailymotion_video

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client("drive_dm_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.text)
async def handle_message(client: Client, message: Message):
    url = message.text.strip()
    await message.reply("🔍 Processing your request...")

    try:
        if "drive.google.com" in url:
            file_path = await download_drive_file(url)
        elif "dailymotion.com" in url:
            file_path = await download_dailymotion_video(url)
        else:
            await message.reply("❌ Invalid URL. Please send a Google Drive or Dailymotion link.")
            return

        await message.reply_document(file_path, caption="✅ File Downloaded and Uploaded")
        os.remove(file_path)
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

if __name__ == "__main__":
    app.run()
