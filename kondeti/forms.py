from django import forms
from .models import Post,comment

class Addpostform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location','image']

class addCommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment_body']