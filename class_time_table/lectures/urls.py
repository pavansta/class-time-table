from django.urls import path

from . import views

urlpatterns = [
    path('', views.lectures, name='lectures'),
    path('add', views.add_lectures, name='add-lectures')
]