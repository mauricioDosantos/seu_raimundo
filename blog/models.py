from django.contrib.auth.models import User
from django.db import models

from colorfield.fields import ColorField


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    publiched_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    attachment_id = models.ManyToManyField(
        'Attachment', verbose_name='Anexos', blank=True, null=True
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Autor'
    )
    tag_id = models.ManyToManyField(
        'Tag', verbose_name='Categorias', blank=True, null=True
    )

    def __str__(self):
        return self.title


class Attachment(models.Model):
    name = models.CharField(max_length=180)
    link = models.CharField(max_length=3000, blank=True, null=True)
    item = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name


# https://pypi.org/project/django-rgbfield/
class Tag(models.Model):
    name = models.CharField(max_length=80)
    color = ColorField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# quatidade de vizualizações da publicação
class Visualized(models.Model):
    ref_date = models.DateField()
    count = models.IntegerField(blank=True, null=True)
    post_id = models.ForeignKey(
        'Post', on_delete=models.CASCADE, verbose_name='Postagem'
    )

    def __str__(self):
        return self.post_id.title


