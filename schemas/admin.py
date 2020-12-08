from django.contrib import admin
from .models import Schema, SchemaField, FieldRow

admin.site.register(Schema)
admin.site.register(SchemaField)
admin.site.register(FieldRow)
