from django.contrib.auth.models import User
from django.db import models

from colorfield.fields import ColorField
from tinymce.models import HTMLField

from account.models import SuperUserCustom


# https://acervolima.com/como-integrar-o-editor-de-texto-personalizado-ao-seu-site-django/
class Post(models.Model):
    title = models.CharField(max_length=250)
    text = HTMLField()
    image = models.ImageField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    publiched_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    attachment_id = models.ManyToManyField(
        'Attachment', verbose_name='Anexos', blank=True
    )
    user_id = models.ForeignKey(
        SuperUserCustom, on_delete=models.CASCADE, verbose_name='Autor'
    )
    tag_id = models.ManyToManyField(
        'Tag', verbose_name='Categorias', blank=True
    )
    area_id = models.ManyToManyField(
        'AreaLabel', verbose_name='Area ou Pastoral', blank=True
    )

    def __str__(self):
        return self.title


class Attachment(models.Model):
    name = models.CharField(max_length=180)
    link = models.CharField(max_length=3000, blank=True, null=True)
    item = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name


# https://pypi.org/project/django-rgbfield/
class Tag(models.Model):
    name = models.CharField(max_length=80)
    color = ColorField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class AreaLabel(models.Model):
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


class Contacts(models.Model):
    name = models.CharField(max_length=180)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    instragram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=500, blank=True, null=True)
    whatsapp = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
