from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(('/home'))
            
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('home')  

