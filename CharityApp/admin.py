from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'user_type']