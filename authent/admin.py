from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your admins here.


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
