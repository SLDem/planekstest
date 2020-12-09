from django.contrib import admin
from django.urls import path, include
from schemas.views import Schemas

urlpatterns = [
    path('', Schemas.as_view()),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('schemas/', include('schemas.urls')),
]
