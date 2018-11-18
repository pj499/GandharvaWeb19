"""GandharvaWeb19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from GandharvaWeb19 import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('home/', views.home, name='home'),
    url('event1/', views.event1, name='event1'),
    url('category1Event1/', views.category1Event1, name='category1Event1'),
]