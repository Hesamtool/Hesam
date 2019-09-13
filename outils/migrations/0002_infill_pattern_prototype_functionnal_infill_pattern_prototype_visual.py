# Generated by Django 2.1.7 on 2019-05-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infill_Pattern_Prototype_Functionnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Pattern Prototype Functionnal',
            },
        ),
        migrations.CreateModel(
            name='Infill_Pattern_Prototype_Visual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Pattern Prototype Visual',
            },
        ),
    ]
