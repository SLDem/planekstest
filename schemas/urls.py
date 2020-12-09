from django.urls import path

from . import views

urlpatterns = [
    path('', views.Schemas.as_view(), name='schemas'),
    path('new-schema/', views.NewSchema.as_view(), name='new_schema'),
    path('schema/<int:pk>/', views.SchemaView.as_view(), name='schema'),
    path('edit-schema/<int:pk>/', views.EditSchema.as_view(), name='edit_schema'),
    path('edit-field/<int:pk>/', views.EditField.as_view(), name='edit_field'),
    path('delete-schema/<int:pk>/', views.DeleteSchema.as_view(), name='delete_schema'),
    path('delete-schema-field/<int:pk>/', views.DeleteSchemaField.as_view(), name='delete_schema_field'),
    path('clear-data/<int:pk>/', views.clear_data, name='clear_data'),
    path('generate-random-schema/<int:pk>/', views.generate_random_schema, name='generate_random_schema'),
    path('get-schema-task-info/', views.get_schema_task_info, name='get_schema_task_info'),
    path('export-data/<int:pk>/', views.export_data, name='export_data'),
]
