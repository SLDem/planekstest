# Generated by Django 3.1.3 on 2020-12-05 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Name')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField()),
                ('field', models.CharField(max_length=10000, verbose_name='Field')),
            ],
        ),
        migrations.CreateModel(
            name='SchemaField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, verbose_name='Name')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schema_fields', to='schemas.schema')),
            ],
        ),
    ]
