# Generated by Django 3.0.5 on 2020-04-10 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeesmanagement', '0003_auto_20200410_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='Imgin',
            new_name='ImageIn',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='Imgout',
            new_name='ImageOut',
        ),
    ]