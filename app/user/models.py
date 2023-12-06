import datetime

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from constants import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name='email', validators=[
            validators.EmailValidator(message="Invalid Email")
        ]
    )
    telephone = models.CharField(
        max_length=50,
        verbose_name='telephone',
        **NULLABLE
    )
    image = models.ImageField(
        upload_to='static.user',
        verbose_name='avatar',
        **NULLABLE
    )
    telegram_user_id = models.IntegerField(**NULLABLE)
    country = models.CharField(
        max_length=50,
        verbose_name='country',
        **NULLABLE
    )
    city = models.CharField(
        max_length=50,
        verbose_name='city',
        **NULLABLE
    )
    is_verified = models.BooleanField(
        verbose_name='is verified',
        default=False
    )
    is_active = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be treated as active. "
                  "Unselect this instead of deleting accounts.",
    )
    date_modified: datetime = models.DateTimeField(
        verbose_name='date modified',
        auto_now=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:

        return f'{self.pk}-{self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('date_joined',)
