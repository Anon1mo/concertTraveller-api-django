from django.urls import path

from . import views

app_name = 'offers'
urlpatterns = [
    path('', views.index, name='index'),
]