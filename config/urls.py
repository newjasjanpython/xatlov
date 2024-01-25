from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('command/', admin.site.urls),
    path('', include('main.urls', '0hb7qY')),
    path('admin/', include('cadmin.urls', 'oR6PcG')),
    path('organization/', include('organizations.urls', 'i8vdYk'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
