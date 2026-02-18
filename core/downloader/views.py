from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        video_url = request.POST.get('url')
        print(video_url)
        
    return render(request, "downloader/home.html")