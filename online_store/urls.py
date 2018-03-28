from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^', include('user_sessions.urls')),
    url(r'^$', views.HomePageView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
