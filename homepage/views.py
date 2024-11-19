from django.shortcuts import render

from homepage.models import Services


def index(request):
   services = Services.objects.filter(is_published=True)
   return render(request, 'homepage/index.html', {'services': services})
