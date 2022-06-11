from django.shortcuts import render
from .models import Profile, Project, Rating
from django.http import HttpResponse

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
    return render(request, 'rater/new_project.html') 


def user_profile(request):
    return render(request, 'rater/user_profile.html')


def update_profile(request):
    return render(request, 'rater/update_profile.html') 


