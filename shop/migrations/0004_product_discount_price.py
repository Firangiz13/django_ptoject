# Generated by Django 3.2.8 on 2021-11-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211107_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(default=0),
        ),
    ]
