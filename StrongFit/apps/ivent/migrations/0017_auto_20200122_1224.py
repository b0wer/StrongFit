# Generated by Django 3.0.2 on 2020-01-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivent', '0016_auto_20200122_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iventuserprofile_photo',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
    ]