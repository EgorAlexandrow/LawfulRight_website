from django.contrib import admin

from homepage.models import Services, Order, Privacy

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'is_published')
    list_filter = ('is_published',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')


@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('privacy_title', 'is_published')
