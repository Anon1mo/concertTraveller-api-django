from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'tests'
urlpatterns = [
    url(r'^tests/hello/?$', views.hello),
    url(r'^tests/fibonnaci/(?P<number>[0-9]+)/$', views.fibonnaci)
]

urlpatterns = format_suffix_patterns(urlpatterns)