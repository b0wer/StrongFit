# Generated by Django 3.0.2 on 2020-01-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivent', '0023_auto_20200130_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivent',
            name='image_logo',
            field=models.ImageField(blank=True, upload_to='IventLogo', verbose_name='Изображение'),
        ),
    ]
