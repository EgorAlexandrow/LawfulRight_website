from django.contrib import admin

from homepage.models import Services

@admin.register(Services)
class ServocesAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'is_published')
    list_filter = ('is_published',)
