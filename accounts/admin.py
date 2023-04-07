from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'age', 'address', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
        (None, {'fields': ('address',)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
        (None, {'fields': ('address',)}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
