# Generated by Django 2.1.7 on 2019-07-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outils', '0013_auto_20190614_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='rack_filling',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='rack_height',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
