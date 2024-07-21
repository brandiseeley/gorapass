from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate_stamps_datatable', views.populate_stamps_datatable, name='populate_stamps_datatable'),
    path('populate_hikes_datatable', views.populate_hikes_datatable, name='populate_hikes_datatable'),
    path('empty_hikes_datatable', views.empty_hikes_datatable, name='empty_hikes_datatable'),
]