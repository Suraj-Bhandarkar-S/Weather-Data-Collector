# Generated by Django 2.1.5 on 2019-02-12 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0011_auto_20190211_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
