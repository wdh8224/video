from django.shortcuts import render


def request(request):
    return render(request, 'index.html')


def request_detail(request):
    return render(request, 'video-page.html')


def upload(request):
    return render(request, 'upload-video.html')


def channels(request):
    return render(request, 'channels.html')


def upload_video(request):
    return render(request, 'channels.html')


def logout(request):
    return render(request, 'login.html')
