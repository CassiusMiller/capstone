from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_property_manager = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)
# Create your models here.
