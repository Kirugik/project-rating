from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('project-details/', views.project_details, name='project-details'),
    path('project-review/', views.project_review, name='project-review'),
    path('new-project/', views.new_project, name='new-project'),
    path('search/', views.search_project, name='search'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('update-profile/', views.project_details, name='update-profile'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 