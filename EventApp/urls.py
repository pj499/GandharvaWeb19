from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^events/$',views.event, name='events'),
    url(r'^events/details/$', views.details, name='details'),
    url(r'^contactus/$', views.contactus, name='contactus'),
]
