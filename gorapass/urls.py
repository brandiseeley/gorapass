from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hikes', views.hikes, name='hikes'),
    path('stamps', views.stamps, name='stamps'),
    path('hikes/<int:hike_id>', views.hike, name='hike'),
    path('users/<int:user_id>', views.user, name='user'),
    path('users/<int:user_id>/completed_hikes', views.user_completed_hikes, name='user_completed_hikes'),
    path('users/login', views.login_user, name='login'),
    path('users/logout', views.logout_user, name='logout'),
    path('users/login_test_user', views.login_test_user, name="login_test_user"),
    path('populate_stamps_datatable', views.populate_stamps_datatable, name='populate_stamps_datatable'),
    path('populate_hikes_datatable', views.populate_hikes_datatable, name='populate_hikes_datatable'),
    path('empty_hikes_datatable', views.empty_hikes_datatable, name='empty_hikes_datatable'),
]