from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.conf import settings


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    avatar = models.ImageField()

    def __str__(self):
        return self.username


class Catalog(models.Model):
    first_preview = models.ImageField(blank=True, upload_to='catalog-preview/')
    second_preview = models.ImageField(blank=True, upload_to='catalog-preview/')
    third_preview = models.ImageField(blank=True, upload_to='catalog-preview/')
    title = models.CharField(max_length=50)
    text = models.TextField()
    cost = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=now())
    in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Projects(models.Model):
    preview = models.ImageField(upload_to='project-preview/')
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=now())
    likes = models.ManyToManyField(CustomUser, related_name='like', default=None, blank=True)
    likes_count = models.IntegerField(default=0)
    author = models.ForeignKey(
        blank=True,
        to=CustomUser,
        on_delete=models.CASCADE,
        default=0,
    )
    def __str__(self):
        return self.title


class Comments(models.Model):
    text = models.TextField(default='')
    author = models.ForeignKey(
        'auth2.CustomUser',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE
    )


class Requests(models.Model):
    author = models.ForeignKey(
        blank=True,
        to=CustomUser,
        on_delete=models.CASCADE,
        default=0,
    )
    text = models.TextField()
    sending_date = models.DateTimeField(default=now())
    phone = models.CharField(max_length=15)
