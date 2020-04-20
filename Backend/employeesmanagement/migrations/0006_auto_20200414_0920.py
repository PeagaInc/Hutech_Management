# Generated by Django 3.0.5 on 2020-04-14 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeesmanagement', '0005_auto_20200411_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Status',
            field=models.CharField(choices=[('Checked In', 'Checked In'), ('Checked Out', 'Checked Out')], default='Enable', max_length=15),
        ),
        migrations.AlterField(
            model_name='faceencoding',
            name='Employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeesmanagement.Employee', unique=True),
        ),
    ]