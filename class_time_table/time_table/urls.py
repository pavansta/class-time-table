from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='time_table'),
    path('submit', views.submit, name='save-time-table'),
    path('delete', views.delete_everything, name='delete-time-table')
]