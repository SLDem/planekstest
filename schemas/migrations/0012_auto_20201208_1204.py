# Generated by Django 3.1.3 on 2020-12-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0011_auto_20201208_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemafield',
            name='end',
            field=models.IntegerField(blank=True, default=50, null=True),
        ),
        migrations.AlterField(
            model_name='schemafield',
            name='start',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]