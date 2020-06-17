from django import forms 
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  ['title', 'author_description', 'image', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'content']

