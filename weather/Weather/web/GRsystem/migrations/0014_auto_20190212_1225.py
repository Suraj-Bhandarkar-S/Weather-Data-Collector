# Generated by Django 2.1.5 on 2019-02-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0013_complaint_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.IntegerField(choices=[(1, 'Solved'), (2, 'Pending')], default=2),
        ),
    ]