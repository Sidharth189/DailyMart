# Generated by Django 4.1.7 on 2023-05-30 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserModule', '0006_shippingaddressdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddressdb',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='UserModule.userdb'),
        ),
    ]
