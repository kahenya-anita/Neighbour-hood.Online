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

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'hood']



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','post_description','posted_by')