# Generated by Django 2.1.7 on 2019-06-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outils', '0006_result_layer_height_mate'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='pattern_support_cost',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='pattern_support_mate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
