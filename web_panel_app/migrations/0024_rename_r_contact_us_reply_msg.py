# Generated by Django 4.2.4 on 2023-09-08 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_panel_app', '0023_remove_order_cart_order_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_us',
            old_name='r',
            new_name='reply_msg',
        ),
    ]
