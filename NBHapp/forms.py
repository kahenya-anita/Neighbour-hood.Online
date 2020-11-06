from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create your forms here
class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'description', 'location', 'population', 'image']

class Hood(forms.ModelForm):
    class Meta:
        model = Hood
        fields = '__all__'
        

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name','hood')

class AddBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name','email','neighbourhood')

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','post_description',)