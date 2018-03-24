from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
