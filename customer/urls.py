
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_customer, name='add_customer'),
    url(r'^view/$', views.view_customer, name='view_customer'),
    url(r'^edit/$', views.edit_customer, name='edit_customer'),
    url(r'^delete/$', views.delete_customer, name='delete_customer'),
]
