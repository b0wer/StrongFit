# Generated by Django 3.0.2 on 2020-01-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivent', '0021_ivent_image_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivent',
            name='IventUserProfils',
            field=models.ManyToManyField(default=None, to='ivent.IventUserProfile', verbose_name='Профиль участника'),
        ),
    ]