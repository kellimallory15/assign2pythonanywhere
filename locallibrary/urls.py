from django.contrib import admin
from django.urls import path, include, repath
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
    settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
    settings.STATIC_ROOT}), #serve static files when deployed
    path('', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('register.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
