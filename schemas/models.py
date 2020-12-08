from django.db import models


class Schema(models.Model):
    objects = models.Manager()

    name = models.CharField('Name', max_length=70)
    entries = models.IntegerField('Entries', default=0)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(null=True)

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_schemas', null=True)


class SchemaField(models.Model):
    objects = models.Manager()

    NAME = 'Name'
    AGE = 'Age'
    EMAIL = 'Email'
    PHONE = 'Phone'
    RANGE_INTEGER = 'Range Integer'
    FIELD_CHOICES = [
        (NAME, 'Name'),
        (AGE, 'Age'),
        (EMAIL, 'Email'),
        (PHONE, 'Phone'),
        (RANGE_INTEGER, 'Range Integer'),
    ]

    start = models.IntegerField(default=1, null=True, blank=True)
    end = models.IntegerField(default=50, null=True, blank=True)

    value = models.CharField('Name', max_length=100)
    type = models.CharField(max_length=13, choices=FIELD_CHOICES, default=NAME)

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='schema_fields')


class FieldRow(models.Model):
    objects = models.Manager()

    data = models.CharField('Data', max_length=5000)
    field = models.ForeignKey(SchemaField, on_delete=models.CASCADE, related_name='field_rows')
