from django import forms 
from .models import Project


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_image', 'description', 'technologies_used', 'link'] 
    