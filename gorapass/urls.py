from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('populate_database', views.populate_database, name='populate_database')
]