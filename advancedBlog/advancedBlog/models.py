from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.categoryName
    
    def get_absolute_url(self):
        return reverse('home')

    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    tag = models.CharField(max_length = 150)
    like = models.ManyToManyField(User, related_name='blogPost')
    category = models.CharField(max_length = 150)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.author) + " | " + self.title
    
    def get_absolute_url(self):
        return reverse('home')

    def totalLikes(self):
        return self.like.count()

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name = "comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.post.title + " | " + self.name
    