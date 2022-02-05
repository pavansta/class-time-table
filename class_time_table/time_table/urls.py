from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='time_table'),
    path('data', views.details, name='table-details'),
    path('', views.index, name='department')
]