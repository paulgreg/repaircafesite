from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Request
from .models import Profile


class RequestAdmin(admin.ModelAdmin):
    date_hierarchy = 'reparation_date'
    list_display = ('reparation_date', 'user', 'category_text',
                    'brand_text', 'token_url')

    def token_url(self, obj):
        url = reverse('repaircafeapp:edit', kwargs={'token': obj.token_text})
        return format_html("<a href='{url}' target='blank'>{url}</a>", url=url)


admin.site.register(Request, RequestAdmin)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
