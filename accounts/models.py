from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class TransferStatusTypeOption(models.TextChoices):
    ADMIN = 'admin', 'admin'
    BP = 'bp', 'bp'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    address = models.CharField(max_length=50)
    type = models.CharField(max_length=15, choices=TransferStatusTypeOption.choices)

    def __str__(self):
        return self.email