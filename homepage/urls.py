from django.urls import path

from . import views


app_name = 'homepage'

urlpatterns = [
    path('cookies/', views.cookies, name='cookies'),
    path('', views.index, name='index')
]
