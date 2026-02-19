from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse

import yt_dlp
import os


# Create your views here.
def home(request):
    if request.method == "POST":
        video_url = request.POST.get('url')

        filepath = download_video(video_url)

        return FileResponse(open(filepath, 'rb'), as_attachment=True)
        
    return render(request, "downloader/home.html")

def download_video(url):
    ydl_opts = {
        'outtmpl':os.path.join(settings.MEDIA_ROOT, '%(title)s.%(ext)s'),
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download =True)
        filename = ydl.prepare_filename(info)

        return filename