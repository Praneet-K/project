from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class DateInput(forms.DateInput):
    input_type= 'date'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    CHOICES = [('M','Male'),('F','Female'),('U','Unknown')]
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    dob = forms.DateField(widget=DateInput(attrs={'type':'date','title':'mm/dd/yyyy','placeholder':'mm/dd/yyyy'}))
    #dob = forms.DateField(widget=forms.SelectDateWidget(attrs={'type':'date'}))
    class Meta:
        model = Profile
        fields = ['image','phno','state','university','sem','dob','gender']