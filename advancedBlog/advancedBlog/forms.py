from django import forms
from .models import Post, Category, Comments

categoryChoices = Category.objects.all().values_list('categoryName', 'categoryName')
categoryChoiceList = []

for item in categoryChoices:
    categoryChoiceList.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'category', 'image', 'description']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categoryChoiceList, attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'category', 'image', 'description']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categoryChoiceList, attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryName']
        
        widgets = {
            'categoryName': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'categoryName': 'Category Name',
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'comment']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }