# Generated by Django 4.1.2 on 2022-11-19 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0035_alter_bid_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('Verified', 'Verified'), ('Unverified', 'Unverified')], max_length=200, null=True),
        ),
    ]