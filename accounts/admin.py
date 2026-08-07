from .models import Profile

from django.contrib import admin

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone', 'city', 'country')
    search_fields = ('user__username', 'phone', 'city',)