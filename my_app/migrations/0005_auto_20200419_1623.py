# Generated by Django 3.0.5 on 2020-04-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20200419_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='medalType',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='url',
        ),
        migrations.AddField(
            model_name='bank',
            name='bank_url',
            field=models.CharField(default='heello.com', max_length=200),
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_url',
            field=models.CharField(default='heello.com', max_length=250),
        ),
    ]
