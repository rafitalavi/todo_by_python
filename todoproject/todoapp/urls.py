from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    # path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('complete/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),

]