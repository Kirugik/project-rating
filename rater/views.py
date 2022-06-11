from django.shortcuts import render, redirect
from .models import Profile, Project, Rating
from .forms import NewProjectForm
from django.http import HttpResponse 
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer, RatingSerializer 

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'rater/index.html', context)


def project_details(request):
    return render(request, 'rater/project_details.html')


def project_review(request):
    return render(request, 'rater/project_review.html')


def search_project(request):
    return render(request, 'rater/search.html')


def new_project(request):
    current_user = request.user
    
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = current_user
            new_project.save()
        return redirect('index') 
    else:
        form = NewProjectForm()
    context = {'form': form, 'current_user': current_user}
    return render(request, 'rater/new_project.html', context)  


def user_profile(request):
    return render(request, 'rater/user_profile.html')


def update_profile(request):
    return render(request, 'rater/update_profile.html') 



class ProfilesList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all() 
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response (serializers.data)


class ProjectsList(APIView):
    def get(self, request, format=None): 
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response (serializers.data)


