from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    
    path('register/', views.registerUser, name='register'), 
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('project-details/', views.project_details, name='project-details'),
    path('project-review/<int:id>', views.project_review, name='project-review'),
    path('new-project/', views.new_project, name='new-project'),

    path('search/', views.search_project, name='search'), 

    path('user-profile/', views.user_profile, name='user-profile'),
    path('update-profile/', views.update_profile, name='update-profile'),  

    path('projectrating/api/profiles/', views.ProfilesList.as_view(), name='profiles-api'),
    path('projectrating/api/projects/', views.ProjectsList.as_view(), name='projects-api'),  
    path('projectrating/', views.profile_project_api, name='projectrating'),  
]  

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 