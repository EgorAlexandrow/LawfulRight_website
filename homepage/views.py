from django.shortcuts import render

from homepage.models import Services, Cookies


def index(request):
    services = Services.objects.filter(is_published=True)
    return render(request, 'homepage/index.html', {'services': services})


def cookies(request):
    cookies_files = Cookies.objects.filter(is_published=True)
    return render(request, 'homepage/cookies.html', {'cookies_files': cookies_files})
