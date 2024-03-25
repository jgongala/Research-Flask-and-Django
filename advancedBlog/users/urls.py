from django.urls import path
from .views import UserRegister, ChangePassword, UserProfile

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('password/', ChangePassword.as_view(), name='passwordChange'),
    path('editProfile/', UserProfile.as_view(), name='editProfile'),
]
