from __future__ import absolute_import, unicode_literals
import string
import random
from django.utils.crypto import get_random_string
from celery import shared_task, current_task

from .models import Schema, SchemaField, FieldRow


@shared_task
def create_schema(total_entries, pk):
    schema = Schema.objects.get(pk=pk)
    fields = SchemaField.objects.filter(schema=schema)
    for i in range(total_entries):
        for field in fields:
            value = ""
            if field.type == 'Name':
                value = get_random_string(random.randint(3, 20), string.ascii_letters) + ' ' + \
                           get_random_string(random.randint(3, 20), string.ascii_letters)
            elif field.type == 'Email':
                value = '%s@gmail.com' % get_random_string(20, string.ascii_letters)
            elif field.type == 'Age':
                value = random.randint(1, 120)
            elif field.type == 'Phone':
                n = '0000000000'
                while '9' in n[3:6] or n[3:6] == '000' or n[6] == n[7] == n[8] == n[9]:
                    n = str(random.randint(10 ** 9, 10 ** 10 - 1))
                value = n[:3] + '-' + n[3:6] + '-' + n[6:]
            elif field.type == 'Range Integer':
                value = random.randint(field.start, field.end)

            row = FieldRow.objects.create(data=value, field=field)
            row.save()
            current_task.update_state(state='PROGRESS',
                                      meta={'current': i, 'total': total_entries,
                                            'percent': int((float(i) / total_entries) * 100)})
    return {'current': total_entries, 'total': total_entries, 'percent': 100}
