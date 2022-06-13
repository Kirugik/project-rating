from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User 
from .models import Project, Profile


class NewProjectForm(ModelForm):
    class Meta:
        model = Project 
        fields = ['project_name', 'project_image', 'description', 'technologies_used', 'link']
        exclude = ['pub_date', 'profile', 'user_id'] 


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname', 'profile_picture', 'bio', 'location', 'contact']
        exclude = ['user']  


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  
    