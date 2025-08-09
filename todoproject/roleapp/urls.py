from django.urls import path
from . import views

urlpatterns = [
    path('', views.roleindex, name='roleindex'),
    path('edit/<int:pk>/', views.role_edit, name='role_edit'),
    

]