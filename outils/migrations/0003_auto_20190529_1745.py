# Generated by Django 2.1.7 on 2019-05-29 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outils', '0002_infill_pattern_prototype_functionnal_infill_pattern_prototype_visual'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='infill_patt_proto_func',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outils.Infill_Pattern_Prototype_Functionnal'),
        ),
        migrations.AddField(
            model_name='printer',
            name='infill_patt_proto_visu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outils.Infill_Pattern_Prototype_Visual'),
        ),
    ]
