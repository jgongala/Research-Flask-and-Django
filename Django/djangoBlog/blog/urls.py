from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('createPost/', views.createPost, name="createPost"),
    path('delete/<int:post_id>/', views.delete, name="delete"),
    path('edit/<int:post_id>/', views.edit, name="edit")
]
