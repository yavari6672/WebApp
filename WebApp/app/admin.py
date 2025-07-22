from django.contrib import admin
from .models import App


class AppAdmin(admin.ModelAdmin):
    list_display = ("app_name",  "description", "create_date", "enabled",)


admin.site.register(App, AppAdmin)
