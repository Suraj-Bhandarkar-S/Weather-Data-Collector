# Generated by Django 2.2 on 2019-04-30 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0022_graph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='Date',
            field=models.DateField(),
        ),
    ]
