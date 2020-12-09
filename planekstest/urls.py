from django.contrib import admin
from django.urls import path, include
from schemas.views import Schemas
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', Schemas.as_view()),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('schemas/', include('schemas.urls')),
]
urlpatterns += static('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )