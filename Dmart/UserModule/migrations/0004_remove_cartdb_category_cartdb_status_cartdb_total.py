# Generated by Django 4.1.7 on 2023-05-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserModule', '0003_cartdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='category',
        ),
        migrations.AddField(
            model_name='cartdb',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartdb',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]