# Generated by Django 2.1.7 on 2019-06-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outils', '0007_auto_20190613_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='infill_label_suppo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]