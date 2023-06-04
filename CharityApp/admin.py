from django.contrib import admin
from .models import CustomUser, Organization, Donation

# Register your models here.
@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'user_type']

@admin.register(Organization)
class OrganizationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','name', 'image', 'description', 'mission', 'country']

@admin.register(Donation)
class DonationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'donor', 'organization', 'amount', 'date']


