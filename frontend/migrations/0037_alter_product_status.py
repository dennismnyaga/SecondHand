# Generated by Django 4.1.2 on 2022-11-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0036_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]