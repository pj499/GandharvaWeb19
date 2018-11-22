from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^events/$',views.event, name='events'),
    url(r'^events/details/$', views.details, name='details'),
    url(r'^sw.js', (TemplateView.as_view(
        template_name="sw.js",
        content_type='application/javascript',
    )), name='sw.js'),
]
