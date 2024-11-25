from django.urls import path

from . import views


app_name = 'homepage'

urlpatterns = [
    path('send_order_form/', views.send_order_form, name='send_order_form'),
    path('', views.index, name='index')
]
