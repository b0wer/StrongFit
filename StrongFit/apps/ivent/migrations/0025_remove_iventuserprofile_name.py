# Generated by Django 3.0.2 on 2020-01-30 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivent', '0024_auto_20200130_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iventuserprofile',
            name='name',
        ),
    ]
