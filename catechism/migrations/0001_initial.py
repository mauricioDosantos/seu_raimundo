# Generated by Django 4.0.1 on 2022-03-01 19:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.CharField(default='9 - 10', max_length=300, verbose_name='Faixa etária')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Numero da Sala')),
                ('description', models.CharField(default='Centro catequético - Matriz', max_length=300, verbose_name='Localização')),
            ],
        ),
        migrations.CreateModel(
            name='CatechismRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70, verbose_name='Nome Completo')),
                ('data_nas', models.DateField(verbose_name='Data de Nascimento')),
                ('district', models.CharField(max_length=40, verbose_name='Bairro')),
                ('street', models.CharField(max_length=80, verbose_name='Rua')),
                ('num_house', models.IntegerField(verbose_name='Número da Casa')),
                ('local_batismo', models.CharField(blank=True, max_length=80, null=True, verbose_name='Local de Batismo')),
                ('data_batismo', models.DateField(blank=True, null=True, verbose_name='Data de Batismo')),
                ('celular', models.CharField(max_length=30, verbose_name='Celular')),
                ('batismo', models.BooleanField(default=False, verbose_name='É Batizado?')),
                ('pri_eucaristia', models.BooleanField(default=False, verbose_name='Fez a Primeira Eucaristia?')),
                ('crisma', models.BooleanField(default=False, verbose_name='Recebeu o Crisma?')),
                ('mom_name', models.CharField(max_length=70, verbose_name='Nome do Pai')),
                ('father_name', models.CharField(max_length=70, verbose_name='Nome da Mãe')),
                ('estado_civil', models.CharField(choices=[('casados', 'Casados'), ('juntos(não casado)', 'União de fato'), ('divorciados', 'Divorciado(a)'), ('viúvo', 'Viúvo(a)'), ('solteiro', 'Solteiro(a)')], default='casados', max_length=30, verbose_name='Estado Civil')),
                ('observation', models.TextField(default='sem observações', verbose_name='Observações')),
                ('amount', models.BooleanField(default=False, verbose_name='Taxa')),
                ('subscription_date', models.DateField(default=datetime.datetime.now, verbose_name='Data de Inscrição')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Catequista')),
            ],
        ),
        migrations.CreateModel(
            name='CatechismCalss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição da turma')),
                ('year', models.DateField(blank=True, null=True)),
                ('age_group_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catechism.agegroup', verbose_name='Faixa etária')),
                ('catechism_register_id', models.ManyToManyField(blank=True, to='catechism.CatechismRegister', verbose_name='Catequisandos')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catechism.room', verbose_name='Local')),
                ('user_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Catequistas')),
            ],
        ),
    ]
