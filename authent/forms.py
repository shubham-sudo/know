from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext as _

from .models import CustomUser


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.TextInput(attrs={'autofocus': True}),
        help_text=_('Enter emial address to register'),
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
