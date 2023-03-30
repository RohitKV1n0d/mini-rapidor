from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_order, name='add_order'),
    url(r'^list/$', views.list_order, name='list_order'),
    url(r'^edit_discount/$', views.edit_order_discount, name='edit_order_discount'),
    url(r'^edit_orderline/(?P<id>\d+)/$', views.edit_orderline, name='edit_orderline'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_order, name='delete_order'),
    url(r'^delete/orderline/(?P<id>\d+)/$', views.delete_orderline, name='delete_orderline'),
    url(r'^list/customers/$', views.list_customers, name='list_customers')
]
    