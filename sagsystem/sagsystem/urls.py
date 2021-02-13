# DjangoImports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# End DjangoImports


# Urls
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('mainapp.urls')),
    path('incidents/', include('incidents.urls')),
    path('tender/', include('tender.urls')),
    path('customers/', include('customers.urls')),
]
# End Urls

# StaticForDebug
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# End StaticForDebug
