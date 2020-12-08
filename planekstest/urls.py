from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from schemas.views import Schemas

urlpatterns = [
    path('', Schemas.as_view()),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('schemas/', include('schemas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)