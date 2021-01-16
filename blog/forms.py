from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')