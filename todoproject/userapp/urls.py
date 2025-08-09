from django.urls import path
from . import views

app_name = 'userapp'
urlpatterns = [
    path('users/', views.user_list, name='user_list'),                 # List all users
    path('users/create/', views.create_user, name='create_user'),      # Create user
    path('users/<int:user_id>/', views.user_detail, name='user_detail'), # User detail
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'), # Edit user
    path('users/<int:user_id>/password/', views.change_password, name='change_password'), 
]