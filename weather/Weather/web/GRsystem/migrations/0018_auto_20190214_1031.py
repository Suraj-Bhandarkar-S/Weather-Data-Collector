# Generated by Django 2.1.5 on 2019-02-14 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0017_auto_20190214_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='collegename',
            field=models.CharField(choices=[('Canara', 'school1'), ('Howard', 'school2')], max_length=7),
        ),
    ]
