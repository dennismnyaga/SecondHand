# Generated by Django 4.1.2 on 2022-11-06 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0019_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='photo',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='frontend.product'),
            preserve_default=False,
        ),
    ]