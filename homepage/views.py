from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from homepage.models import Services, Privacy
from homepage.forms import OrderForm


def index(request):
    if not request.COOKIES.get('open_site'):
        response = HttpResponse("Открытие сайта!")
        response.set_cookie('open_site', 'true', max_age=3600)
    services = Services.objects.filter(is_published=True)
    form = OrderForm()
    return render(request, 'homepage/index.html', {'services': services, 'form': form})


def privacy_policy(request):
    privacy = Privacy.objects.filter(is_published=True)
    return render(request, 'includes/privacy_policy.html', {'privacy': privacy})


def send_order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            problem = form.cleaned_data['problem']
            confidential = form.cleaned_data['confidential']

            subject = 'Новая заявка'
            message = f'Имя: {name}\nТелефон: {phone}\nEmail: {email}\nПроблема: {problem}\nСогласие с политикой конфиденциальности: {"Да" if confidential else "Нет"}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, recipient_list)

            form.save()
            return redirect('homepage:index')
    else:
        form - OrderForm()
    return render(request, 'homepage/index.html', {'form': form})
