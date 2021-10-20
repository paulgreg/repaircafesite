from django.utils.html import format_html
from django.contrib import admin
from django.urls import reverse
from .models import Request


class RequestAdmin(admin.ModelAdmin):
    date_hierarchy = 'reparation_date'
    list_display = ('reparation_date', 'name_text', 'firstname_text', 'locality_text',
                    'category_text', 'brand_text', 'token_url')

    def token_url(self, obj):
        url = reverse('repaircafeapp:edit', kwargs={'token': obj.token_text})
        return format_html("<a href='{url}' target='blank'>{url}</a>", url=url)


admin.site.register(Request, RequestAdmin)
