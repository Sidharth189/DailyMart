# Generated by Django 4.1.7 on 2023-05-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserModule', '0004_remove_cartdb_category_cartdb_status_cartdb_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
