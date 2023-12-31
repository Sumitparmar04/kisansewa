# Generated by Django 4.1.4 on 2023-08-22 13:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_panel_app', '0002_rename_variey_desc_seed_variety_type_variety_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('cat_img', models.FileField(blank=True, default='', null=True, upload_to='seed_cat_image')),
                ('cat_desc', models.TextField(blank=True, default='', null=True)),
                ('delete_status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(blank=True, max_length=50, null=True)),
                ('pro_img', models.ImageField(blank=True, null=True, upload_to='product')),
                ('pro_desc', models.TextField(blank=True, null=True)),
                ('pro_price', models.CharField(blank=True, max_length=50, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('varient', models.IntegerField(default=0)),
                ('discount_price', models.CharField(blank=True, max_length=50, null=True)),
                ('qty_type', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('delete_status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_cat_name', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_cat_img', models.ImageField(blank=True, null=True, upload_to='sub_category')),
                ('sub_cat_desc', models.TextField(blank=True, null=True)),
                ('delete_status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_panel_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanity', models.FloatField(blank=True, default=0, null=True)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seed_volume', to='web_panel_app.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='dawai_customer',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='seed_customer',
        ),
        migrations.RemoveField(
            model_name='seed',
            name='seed_cat',
        ),
        migrations.RemoveField(
            model_name='seed',
            name='seed_variety',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Seed',
        ),
        migrations.DeleteModel(
            name='Seed_Category',
        ),
        migrations.DeleteModel(
            name='Seed_Variety_Type',
        ),
        migrations.DeleteModel(
            name='Urvarak_and_Dawai',
        ),
        migrations.AddField(
            model_name='product',
            name='sub_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_panel_app.sub_category'),
        ),
    ]
