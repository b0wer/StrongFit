# Generated by Django 3.0.2 on 2020-01-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivent', '0005_auto_20200114_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ivent',
            name='IventUserProfils',
        ),
        migrations.AddField(
            model_name='ivent',
            name='IventUserProfils',
            field=models.ManyToManyField(to='ivent.IventUserProfile', verbose_name='Профиль участника'),
        ),
    ]
