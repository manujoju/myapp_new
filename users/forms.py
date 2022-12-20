from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    username = forms.CharField(required=True, widget=forms.TextInput())
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.TextInput())
    
    
    class Meta:
        model = User
        fields = ('email','username','password1','password2')
    
