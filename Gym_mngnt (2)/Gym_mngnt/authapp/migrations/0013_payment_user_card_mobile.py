# Generated by Django 3.1.1 on 2023-05-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_payment_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_user',
            name='card_mobile',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
