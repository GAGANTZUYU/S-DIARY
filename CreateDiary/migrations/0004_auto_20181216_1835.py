# Generated by Django 2.1.3 on 2018-12-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDiary', '0003_auto_20181216_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Month',
        ),
        migrations.AddField(
            model_name='profile',
            name='Username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
