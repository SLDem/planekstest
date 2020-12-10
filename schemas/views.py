from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views.generic import FormView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Schema, SchemaField, FieldRow
from .forms import SchemaForm, SchemaFieldForm, GenerateSchemaForm
from .tasks import create_schema

import json
import datetime
import csv

from celery.result import AsyncResult


def generate_random_schema(request, pk):
    schema = Schema.objects.get(pk=pk)
    fields = SchemaField.objects.filter(schema=schema)
    for field in fields:
        rows = FieldRow.objects.filter(field=field)
        rows.delete()

    if request.method == 'POST':
        form = GenerateSchemaForm(request.POST)
        if form.is_valid():
            total_entries = form.cleaned_data['total_entries']
            schema.entries = total_entries
            schema.save()
            task = create_schema.delay(total_entries, schema.pk)
            return HttpResponse(json.dumps({'task_id': task.id}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'task_id': None}), content_type='application/json')
    else:
        form = GenerateSchemaForm()
    return render(request, 'schemas/generate_random_schema.html', {'form': form, 'schema': schema})


def get_schema_task_info(request):
    task_id = request.GET.get('task_id', None)
    if task_id is not None:
        task = AsyncResult(task_id)
        data = {
            'state': task.state,
            'result': task.result,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse('No schema job id given')


def export_data(request, pk):

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)

    schema = Schema.objects.get(pk=pk)
    fields = SchemaField.objects.filter(schema=schema)
    fields_values = []
    field_rows = []

    for field in fields:
        fields_values.append(field.value)

    writer.writerow(fields_values)

    for field in fields:
        for row in field.field_rows.all():
            field_rows.append(row.data)

    # split the rows into chunks that are writable into csv because original data format is unsuitable for that
    n = schema.entries
    rows = [field_rows[i:i + n] for i in range(0, len(field_rows), n)]
    rows = zip(*rows)

    for row in rows:
        writer.writerow(row)

    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    return response


class Schemas(ListView):
    template_name = 'schemas/schemas.html'
    model = Schema
    context_object_name = 'schemas'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            schemas = Schema.objects.filter(user=self.request.user)
        else:
            return redirect('login')
        return schemas


class NewSchema(FormView):
    template_name = 'schemas/new_schema.html'
    form_class = SchemaForm

    def form_valid(self, form):
        schema = form.save(commit=False)
        schema.user = self.request.user
        schema.save()
        return redirect(reverse('schema', kwargs={'pk': schema.pk}))


class SchemaView(DetailView, FormView):
    model = Schema
    form_class = SchemaFieldForm
    template_name = 'schemas/schema.html'
    context_object_name = 'schema'

    def get_context_data(self, **kwargs):
        context = super(SchemaView, self).get_context_data(**kwargs)
        button_status = 'on'
        schema = self.get_object()
        fields = SchemaField.objects.filter(schema=schema)
        for field in fields:
            if not field.field_rows.all():
                button_status = 'off'
        context['button_status'] = button_status
        context['object'] = schema
        return context

    def form_valid(self, form):
        new_field = form.save(commit=False)
        schema = self.get_object()
        new_field.schema = schema
        start = self.request.POST.get('start')
        end = self.request.POST.get('end')
        if start:
            new_field.start = start
        if end:
            new_field.end = end

        new_field.save()
        return redirect('schema', pk=schema.pk)


def clear_data(request, pk):
    schema = Schema.objects.get(pk=pk)
    fields = schema.schema_fields.all()
    for field in fields:
        rows = FieldRow.objects.filter(field=field)
        rows.delete()
    return redirect('schema', pk=schema.pk)


class EditSchema(UpdateView):
    model = Schema
    form_class = SchemaForm
    template_name = 'schemas/edit_schema.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = self.get_object().name
        return initial

    def form_valid(self, form):
        schema = form.save(commit=False)
        schema.date_modified = datetime.date.today()
        schema.save()
        return redirect('schema', pk=schema.pk)


class EditField(UpdateView):
    model = SchemaField
    form_class = SchemaFieldForm
    template_name = 'schemas/edit_field.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['value'] = self.get_object().value
        initial['type'] = self.get_object().type
        return initial

    def form_valid(self, form):
        schema_field = form.save()
        schema = self.get_object().schema
        schema.date_modified = datetime.date.today()
        schema.save()
        return redirect('schema', pk=schema_field.schema.pk)


class DeleteSchema(DeleteView):
    model = Schema

    def get_success_url(self):
        return reverse_lazy('schemas')


class DeleteSchemaField(DeleteView):
    model = SchemaField

    def get_success_url(self):
        schema = self.object.schema
        return reverse_lazy('schema', kwargs={'pk': schema.pk})
