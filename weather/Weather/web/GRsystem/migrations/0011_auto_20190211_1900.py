# Generated by Django 2.1.5 on 2019-02-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0010_auto_20190211_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Type_of_complaint',
            field=models.IntegerField(choices=[(1, 'ClassRoom'), (2, 'Teacher'), (3, 'Management'), (4, 'School'), (5, 'Other')], null=True),
        ),
    ]