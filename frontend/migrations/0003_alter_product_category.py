# Generated by Django 4.1.2 on 2022-10-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_product_current_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Fashion', 'Fashion'), ('More', 'More'), ('Prop', 'Prop'), ('vehicles', 'vehicles')], max_length=200),
        ),
    ]