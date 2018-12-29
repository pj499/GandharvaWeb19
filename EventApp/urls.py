from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^events/$',views.event, name='events'),
    url(r'^events/details/$', views.details, name='details'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

]



