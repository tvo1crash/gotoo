from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_hours = models.IntegerField()
    image_url = models.CharField(max_length=200, null=True, blank=True)
    mini_image_url = models.CharField(max_length=200, null=True, blank=True)
    users = models.ManyToManyField(User, related_name='courses', blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username
