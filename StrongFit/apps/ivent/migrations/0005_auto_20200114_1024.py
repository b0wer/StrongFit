# Generated by Django 3.0.2 on 2020-01-14 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ivent', '0004_auto_20200114_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ivent',
            name='IventUserProfils',
        ),
        migrations.AddField(
            model_name='ivent',
            name='IventUserProfils',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ivent.IventUserProfile', verbose_name='Профиль участника'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='iventuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
        ),
    ]
