# Generated by Django 2.1.7 on 2019-09-09 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outils', '0019_auto_20190724_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='image_45',
            new_name='image_68',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='rotation_45_X',
            new_name='rotation_68_X',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='rotation_45_Y',
            new_name='rotation_68_Y',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='rotation_45_Z',
            new_name='rotation_68_Z',
        ),
    ]