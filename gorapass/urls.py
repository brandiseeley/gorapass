from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stamps/', views.stamps, name='stamps'),
    path('populate_database', views.populate_database, name='populate_database'),
]