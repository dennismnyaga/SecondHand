# Generated by Django 4.1.2 on 2022-11-04 08:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_alter_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=tinymce.models.HTMLField(),
        ),
    ]