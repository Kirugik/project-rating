from django.forms import ModelForm
from .models import Project


class NewProjectForm(ModelForm):
    class Meta:
        model = Project 
        fields = ['project_name', 'project_image', 'description', 'technologies_used', 'link']
        exclude = ['pub_date', 'profile', 'user_id'] 
    