import os
from yt_dlp import YoutubeDL

async def download_dailymotion_video(url):
    os.makedirs("downloads", exist_ok=True)
    filename = "downloads/dailymotion_video.mp4"
    ydl_opts = {
        'outtmpl': filename,
        'format': 'best',
        'quiet': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return filename
