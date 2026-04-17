from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse
from .services.video_service import download_video
from .services.video_service import download_audio

import yt_dlp
import os


# Create your views here.
def home(request):
    print("Método:", request.method)
    if request.method == "POST":
        video_url = request.POST.get('url')
        quality = request.POST.get('quality')
        formato = request.POST.get('formato')
        print("URL:", video_url)
        print("Quality:", quality)
        print("Formato:", formato)
        # ...existing code...
        try:
            if not video_url:
                return render(request, 'downloader/home.html', {'error': 'Informe uma URL'})
            elif formato == 'mp4':
                filepath = download_video(video_url, quality)
                return FileResponse(open(filepath, 'rb'), as_attachment=True)
            
            elif formato == 'mp3':        
                filepath = download_audio(video_url)
                return FileResponse(open(filepath, 'rb'), as_attachment=True)
        except Exception:
            return render(request, "downloader/home.html", { "error": "Error found while downloading the video. Please check the URL and try again." })
    else:
        return render(request, "downloader/home.html")
     