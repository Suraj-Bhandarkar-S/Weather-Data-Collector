# Generated by Django 2.2 on 2019-04-25 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0019_auto_20190216_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grievance',
            name='guser',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Complaint',
        ),
        migrations.DeleteModel(
            name='Grievance',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
