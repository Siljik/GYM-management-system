# Generated by Django 4.1.6 on 2023-05-04 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0027_rename_viewv_video_view_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view_video',
            name='payment',
        ),
    ]
