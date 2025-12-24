from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date")
    search_fields = ("first_name", "last_name", "email", "date")
    list_filter = ("date", "state")
    ordering = ("first_name",)
    readonly_fields = ("state", )


admin.site.register(Form, FormAdmin)
