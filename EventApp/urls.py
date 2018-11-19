from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.event, name='event1'),
    url(r'^category1Event1/$', views.category1Event1, name='category1Event1'),
]
