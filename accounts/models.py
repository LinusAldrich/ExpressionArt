from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

class Diary(models.Model):
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    diary_name = models.CharField(max_length=200, unique=True, null=True)
    diary_description = models.CharField(max_length=32767, null=True)

    def __str__(self):
        return self.diary_name

class Canvas(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    canvas_name = models.CharField(max_length=200, unique=True, null=True)
    canvas_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.canvas_name

class Collage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    collage_name = models.CharField(max_length=200, unique=True, null=True)
    collage_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.collage_name

    