# Generated by Django 3.0.2 on 2020-01-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IventUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Прогресс пользователей')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('mass', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Прогресс пользователей',
            },
        ),
        migrations.AlterField(
            model_name='ivent',
            name='data_start',
            field=models.DateField(verbose_name='Дата старта'),
        ),
        migrations.AlterField(
            model_name='ivent',
            name='data_stop',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.AddField(
            model_name='ivent',
            name='IventUserProfils',
            field=models.ManyToManyField(to='ivent.IventUserProfile', verbose_name='Профиль участника'),
        ),
    ]
