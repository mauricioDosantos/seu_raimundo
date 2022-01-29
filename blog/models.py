from colorfield.fields import ColorField
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField()
    register_date = models.DateTimeField(auto_now_add=True)
    publiched_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    attachment_id = models.ManyToManyField(
        'Attachment', verbose_name='Anexos'
    )
    user_id = models.ForeignKey(
        'Superuser', on_delete=models.CASCADE, verbose_name='Autor'
    )
    tag_id = models.ManyToManyField(
        'Tag', verbose_name='Categorias'
    )


class Attachment(models.Model):
    name = models.CharField(max_length=180)
    link = models.CharField(max_length=3000)
    item = models.FileField(upload_to='uploads/')


# https://pypi.org/project/django-rgbfield/
class Tag(models.Model):
    name = models.CharField(max_length=80)
    color = ColorField()
    active = models.BooleanField(default=True)


# quatidade de vizualizações da publicação
class Visualized(models.Model):
    ref_date = models.DateField()
    count = models.IntegerField()
    post_id = models.ForeignKey(
        'Post', on_delete=models.CASCADE, verbose_name='Postagem'
    )


