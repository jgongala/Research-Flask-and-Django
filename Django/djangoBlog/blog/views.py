from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import LoginForm, UserCreationForm
from django.contrib import messages

def home(request):
    # Render the home template with the user's username and posts
    return render(request, 'home.html')

def login(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a LoginForm instance with the submitted POST data
        form = LoginForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Extract email and password from the form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate the user using the provided email and password
            user = authenticate(request, username=username, password=password)
            
            # Check if authentication was successful
            if user is not None:
                # Log in the user
                auth_login(request, user)
                capitalized_username = username.capitalize()
                return render(request, 'home.html', {'username': capitalized_username})
            else:
                # Authentication failed, add an error message
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        # If the request method is not POST, create an empty LoginForm instance
        form = LoginForm()

    # Render the login.html template with the form
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
        else:
            for errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})