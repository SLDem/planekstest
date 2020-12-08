from django import forms
from .models import Schema, SchemaField
from django.core.validators import MinValueValidator


class SchemaForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'schema-name-input'}))

    class Meta:
        model = Schema
        fields = '__all__'
        exclude = ('date_modified', 'user', 'entries')


class SchemaFieldForm(forms.ModelForm):
    value = forms.CharField(widget=forms.TextInput(attrs={'class': 'schema-field-name-input',
                                                          'placeholder': 'Name'}), label='')
    start = forms.IntegerField(required=False)
    end = forms.IntegerField(required=False)

    class Meta:
        model = SchemaField
        fields = ('type', 'value',)


class GenerateSchemaForm(forms.Form):
    total_entries = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'entries-input'}),
                                       label='Number of entries (Must be more or equal to 2)',
                                       required=True,
                                       validators=[MinValueValidator(2)])
