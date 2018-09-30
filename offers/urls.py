from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'offers'
urlpatterns = [
    url(r'^offers/?$',views.OfferList.as_view()),
    url(r'^offers/(?P<pk>[0-9]+)/?$', views.OfferDetail.as_view()),
    url(r'^offers/(?P<pk>[0-9]+)/join/?$', views.OfferJoin.as_view()),
    url(r'^offers/(?P<pk>[0-9]+)/leave/?$', views.OfferLeave.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
