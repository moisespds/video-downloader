import yt_dlp
import os
from django.conf import settings

def download_video(url):
    ydl_opts = {
        'outtmpl': os.path.join(settings.MEDIA_ROOT, '%(title)s.%(ext)s'),
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download =True)
        filename = ydl.prepare_filename(info)

        return filename