from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "workshop_name", "location", "phone", "is_approved")
    list_filter = ("is_approved", "location")
    search_fields = ("username", "email", "workshop_name")
