from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse
from .services.video_service import download_video

import yt_dlp
import os


# Create your views here.
def home(request):
    print("Método:", request.method)
    if request.method == "POST":
        video_url = request.POST.get('url')
        print("URL:", video_url)
        # ...existing code...
        try:
            if not video_url:
                return render(request, 'downloader/home.html', {'error': 'Informe uma URL'})
            filepath = download_video(video_url)
            return FileResponse(open(filepath, 'rb'), as_attachment=True)
        except Exception:
            return render(request, "downloader/home.html", { "error": "Error found while downloading the video. Please check the URL and try again." })
    else:
        return render(request, "downloader/home.html")
    