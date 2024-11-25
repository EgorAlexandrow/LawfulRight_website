from django.shortcuts import render

from homepage.models import Services, Cookies
from homepage.forms import OrderForm


def index(request):
    cookie = Cookies.objects.filter(is_published=True)
    services = Services.objects.filter(is_published=True)
    form = OrderForm()
    return render(request, 'homepage/index.html', {'cookie': cookie, 'services': services, 'form': form})
