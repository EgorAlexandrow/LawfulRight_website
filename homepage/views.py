from django.shortcuts import render

from homepage.models import Services, Cookies


def index(request):
    cookie = Cookies.objects.filter(is_published=True)
    services = Services.objects.filter(is_published=True)
    return render(request, 'homepage/index.html', {'cookie': cookie, 'services': services})
