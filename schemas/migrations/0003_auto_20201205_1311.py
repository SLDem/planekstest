# Generated by Django 3.1.3 on 2020-12-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0002_schema_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='date_modified',
            field=models.DateField(null=True),
        ),
    ]
