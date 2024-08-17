from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hikes', views.hikes, name='hikes'),
    path('stamps', views.stamps, name='stamps'),
    path('stamps/<int:stamp_id>', views.stamp, name='stamp'),
    path('hikes/<int:hike_id>', views.hike, name='hike'),
    path('users/<int:user_id>', views.user, name='user'),
    path('users/<int:user_id>/completed_hikes', views.user_completed_hikes, name='user_completed_hikes'),
    path('users/<int:user_id>/completed_hikes/add', views.add_completed_hike, name='add_completed_hike'),
    path('users/<int:user_id>/completed_hikes/delete', views.delete_completed_hike, name='delete_completed_hike'),
    path('users/<int:user_id>/completed_stamps', views.user_completed_stamps, name='user_completed_stamps'),
    path('users/<int:user_id>/completed_stamps/add', views.add_completed_stamp, name='add_completed_stamp'),
    path('users/is_authenticated', views.is_authenticated, name='is_authenticated'),
    path('users/login', views.login_user, name='login'),
    path('users/logout', views.logout_user, name='logout'),
    path('users/login_test_user', views.login_test_user, name="login_test_user"),
    path('populate_stamps_datatable', views.populate_stamps_datatable, name='populate_stamps_datatable'),
    path('populate_hikes_datatable', views.populate_hikes_datatable, name='populate_hikes_datatable'),
    path('empty_hikes_datatable', views.empty_hikes_datatable, name='empty_hikes_datatable'),
]
