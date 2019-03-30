from django.shortcuts import render


def enroll_request(request):
    return render(request, 'index.html')
