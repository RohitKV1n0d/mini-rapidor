from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_product, name='add_product'),
    url(r'^list/$', views.list_product, name='list_product'),
    url(r'^edit/$', views.edit_product, name='edit_product'),
    url(r'^delete/$', views.delete_product, name='delete_product'),
]
