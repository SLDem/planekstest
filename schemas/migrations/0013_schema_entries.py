# Generated by Django 3.1.3 on 2020-12-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0012_auto_20201208_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='entries',
            field=models.IntegerField(default=0, verbose_name='Entries'),
        ),
    ]
