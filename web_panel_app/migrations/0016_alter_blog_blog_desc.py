# Generated by Django 4.2.4 on 2023-09-04 10:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_panel_app', '0015_remove_cart_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
