from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Post, Category, Comments
from .forms import PostForm, EditForm, CategoryForm, CommentForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib import messages


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_updated']
    
class PostDetails(DetailView):
    model = Post
    template_name = 'postDetails.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post = context['post']
        totalLikes = post.totalLikes()  
        context["totalLikes"] = totalLikes
        
        return context
    
class CreatePost(CreateView):
    model = Post
    template_name = "createPost.html"
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
class EditPost(UpdateView):
    model = Post
    template_name = "editPost.html"
    form_class = EditForm

class DeletePost(DeleteView):
    model = Post
    template_name = "home.html"
    success_url = reverse_lazy('home')
    

class CreateCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "createCategory.html"
    
    
def CategoryFilter(request, type):
    categoryType = Post.objects.filter(category=type.replace('-', ' '))
    return render(request, 'filteredCategory.html', {'type': type.title().replace('-', ' '), 'categoryType':categoryType})

def Like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
        
    return HttpResponseRedirect(reverse('postDetails', args=[str(pk)]))

class AddComment(CreateView):
    model = Comments
    template_name = "addComment.html"
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']  
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postDetails', kwargs={'pk': self.kwargs['pk']})  

    

