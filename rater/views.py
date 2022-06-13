from django.shortcuts import render, redirect
from .models import Profile, Project, Rating
from .forms import NewProjectForm, UpdateProfileForm
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
    if 'project' in request.GET and request.GET['project']:
        keyword = request.GET.get("project") 
        projects = Project.search_project(keyword)
        message = f"{keyword}"  
        return render(request, 'rater/search.html', {"message": message, "projects": projects, 'keyword': keyword})
    else:
        message = "You haven't searched for any project"

        return render(request, 'rater/search.html', {"message": message})




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
    profile = request.user.profile 
    projects = request.user.profile.project_set.all()


    context = {'profile': profile, 'projects': projects}
    return render(request, 'rater/user_profile.html', context)


def update_profile(request):
    current_user = request.user 
    profile = request.user.profile 
    # profile = Profile.objects.get(id=pk)
    form = UpdateProfileForm(instance=profile) 

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            updated_profile = form.save(commit=False)
            updated_profile.user = current_user
            updated_profile.save()
        return redirect('index')
    else:
        form = UpdateProfileForm()
    
    context = {'current_user': current_user, 'profile': profile, 'form': form} 
    return render(request, 'rater/update_profile.html', context)  



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


