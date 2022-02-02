from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='time-table'),
    path('data', views.details, name='table-details')
]