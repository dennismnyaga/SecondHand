# Generated by Django 4.1.2 on 2022-11-10 15:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0027_rename_products_photo_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={},
        ),
        migrations.RemoveField(
            model_name='bid',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='current_bid',
        ),
        migrations.AddField(
            model_name='bid',
            name='date_bided',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='product_bided',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='frontend.product', verbose_name='product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
