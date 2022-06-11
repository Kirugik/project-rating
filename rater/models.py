from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    fullname = models.CharField(max_length=100, blank=True)  
    profile_picture = models.ImageField(upload_to='profiles/')
    bio = models.TextField(max_length=200, default="My Bio") 
    location = models.CharField(max_length=100, blank=True) 
    contact = models.EmailField(max_length=100, blank=True) 

    def __str__(self):
        return self.user.username



class Project(models.Model):
    project_name = models.CharField(max_length=100)  
    project_image = models.ImageField(upload_to='projects/') 
    description = models.TextField()
    technologies_used = models.CharField(max_length=255, blank=True)  
    pub_date = models.DateTimeField(auto_now_add=True)
    link = models.URLField(null=False) 
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects", blank=True, null=True) 

    def __str__(self):
        return self.project_name  
        
    class Meta:
        ordering=['-pub_date'] 



class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ratings', blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='project_ratings') 
    design_rating = models.IntegerField(choices=[(i,i) for i in range(1,11)], null=True)
    usability_rating = models.IntegerField(choices=[(i,i) for i in range(1,11)], null=True)
    creativity_rating = models.IntegerField(choices=[(i,i) for i in range(1,11)], null=True)
    content_rating = models.IntegerField(choices=[(i,i) for i in range(1,11)], null=True)   
    
    
    def __str__(self):
        return self.project 
        
    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()
    
    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id)
        return ratings 
