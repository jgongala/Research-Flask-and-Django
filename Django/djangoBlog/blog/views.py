from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, PostForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required(login_url="/login")
def home(request):
    # Retrieve all posts from the database
    posts = Post.objects.all() 
    
    return render(request, 'home.html', {'posts': posts})

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

def user_logout(request):
    logout(request)
    return redirect('home')  

@login_required(login_url="/login")
def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
        
    else:
        form = PostForm()
        
    return render(request, 'createPost.html', {"form": form})

def delete(request, post_id):
    # Get the post from the database or return a 404 error if not found
    post = get_object_or_404(Post, id=post_id)

    # Check if the current user is the author of the post
    if request.user.is_authenticated and request.user == post.author:
        # Delete the post from the database
        post.delete()

        # Display a success message
        messages.success(request, 'Post deleted successfully!')
    else:
        # Display an error message if the user is not the author
        messages.error(request, 'You do not have permission to delete this post.')

    # Redirect to the home page or any other desired page
    return redirect('home')

@login_required(login_url="/login")
def edit(request, post_id):
    # Retrieve the post from the database or return a 404 error
    post = get_object_or_404(Post, id=post_id)

    # Check if the current user has permission to edit the post
    if request.user != post.author:
        messages.error(request, 'You do not have permission to edit this post.')
        return redirect('home')

    if request.method == 'POST':
        # Handle form submission
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('home')
    else:
        # Pre-populate the form with the data from the post being edited
        form = PostForm(instance=post)

    return render(request, 'editPost.html', {"form": form, "post": post})
