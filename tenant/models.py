from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Maintance (models.Model):
    title = models.CharField(
        max_length=200
        )
    description = models.TextField(
        blank=True, null=True
        )
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('maintance_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title