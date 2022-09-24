from dataclasses import fields
from django import forms
from blog.models import Comment, Post

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author', 'title', 'text', 'user_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'titlebox textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text', 'user_image')

        widgets = {
            'author': forms.TextInput(attrs={'class':'authorbox textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }

