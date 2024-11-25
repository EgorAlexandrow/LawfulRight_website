from django.contrib import admin

from homepage.models import Services,Order, Cookies

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'is_published')
    list_filter = ('is_published',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')


@admin.register(Cookies)
class CookiesAdmin(admin.ModelAdmin):
    list_display = ('cookies_title', 'is_published')
