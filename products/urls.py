from django.conf.urls import url

from . import views


app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/?$', views.ProductDetailView.as_view(), name='product_detail'),
]
