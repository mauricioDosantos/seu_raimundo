# Generated by Django 4.0.1 on 2022-04-22 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_abstract'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='abstract',
            new_name='main_idea',
        ),
        migrations.AddField(
            model_name='post',
            name='main_tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Main_Tag', to='blog.tag', verbose_name='Tag Principal'),
        ),
    ]