# Generated by Django 3.0.2 on 2020-01-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivent', '0009_auto_20200114_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='iventuserprofile',
            name='Growth',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='iventuserprofile',
            name='Weight',
            field=models.IntegerField(null=True),
        ),
    ]