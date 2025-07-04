from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "tag"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 transition duration-200',
                'placeholder': 'Enter your post title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 transition duration-200',
                'rows': 12,
                'placeholder': 'Write your post content here...'
            }),
            'category': forms.Select(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 transition duration-200'
            }),
            'tag': forms.SelectMultiple(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 transition duration-200',
                'size': 4
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 transition duration-200',
                'rows': 4,
                'placeholder': 'Share your thoughts...'
            })
        }
