# Generated by Django 3.0.5 on 2020-04-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_auto_20200419_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_url',
            field=models.CharField(max_length=250),
        ),
    ]
