"""Database models"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    
    def create_user(self, first_name, last_name, email, password=None, **other_fields):
        """Create and save users"""
        username = ''
        other_fields.setdefault('first_name', first_name)
        other_fields.setdefault('last_name', last_name)
        if not email:
            raise ValueError('This given email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(first_name, last_name, email, password, **other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('user name'), max_length=150, blank=True)
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(
        _('email'),
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
