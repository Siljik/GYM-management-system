# Generated by Django 4.1.6 on 2023-05-04 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0029_cart_cartproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='customer',
            new_name='user',
        ),
    ]
