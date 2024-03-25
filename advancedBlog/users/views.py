from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from . forms import RegistrationForm, EditProfileForm, PasswordChangeForm
from django.contrib import messages


# Create your views here.
class UserRegister(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        # Add success message
        messages.success(self.request, "Profile successfully registered.")
        return super().form_valid(form)

class UserProfile(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editProfile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        # Add success message
        messages.success(self.request, "Profile successfully updated.")
        return super().form_valid(form)

class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='registration/changePassword.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        # Add success message
        messages.success(self.request, "Your password has been successfully changed.")
        return super().form_valid(form)


