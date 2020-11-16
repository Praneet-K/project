from django import forms
from .models import Post

class Addpostform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location','image']