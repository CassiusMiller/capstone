from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        max_length=200
    )
    body = models.TextField()
    Location = models.ForeignKey(
        Location, on_delete=models.CASCADE
    )
    Status = models.ForeignKey(
        Status, on_delete=models.CASCADE
    )
    Type = models.ForeignKey(
        Type, on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title