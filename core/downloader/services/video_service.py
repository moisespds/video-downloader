import yt_dlp
import os
from django.conf import settings

def download_video(url, quality):
    ydl_opts = {
        'outtmpl': os.path.join(settings.MEDIA_ROOT, '%(title)s - %(height)s.%(ext)s'),
        'format': quality,
        'merge_output_format': 'mp4',
        'verbose': True,
    }
    print("URL FUNC:", url)
    print("Quality FUNC:", quality)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

        return filename
    
def download_audio(url):
    ydl_opts = {
        'outtmpl': os.path.join(settings.MEDIA_ROOT, '%(title)s.%(ext)s'),  # Save as MP3
        'format': 'bestaudio',  # Downloads best audio quality 
        'postprocessors': [{  # Post-process to convert format if needed
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '320',  # 320 kbps quality
        }],
        'verbose': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        filename = os.path.splitext(filename)[0] + '.mp3'  # Change extension to .mp3
        print("Audio downloaded:", filename)
        print("Audio URL:", url)
        print("Audio options:", ydl_opts)
  
        return filename
    
