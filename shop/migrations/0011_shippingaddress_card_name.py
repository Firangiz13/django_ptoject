# Generated by Django 3.2.8 on 2021-12-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20211207_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='card_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
