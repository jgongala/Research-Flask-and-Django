from django.urls import include, path
from .views import Home, CreatePost, EditPost, PostDetails, DeletePost, CreateCategory, CategoryFilter, Like, AddComment


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('createPost/', CreatePost.as_view(), name='createPost'),
    path('post/editPost/<int:pk>/', EditPost.as_view(), name='editPost'),
    path('post/<int:pk>/', PostDetails.as_view(), name='postDetails'),
    path('post/delete/<int:pk>/', DeletePost.as_view(), name='deletePost'),  
    path('createCategory', CreateCategory.as_view(), name='createCategory'), 
    path('like/<int:pk>', Like, name='likedPost'), 
    path('category/<str:type>', CategoryFilter, name='categoryFilter'),
    path('<int:uid>/', include('users.urls')),
    path('post/<int:pk>/addComment/', AddComment.as_view(), name='addComment'),
]
