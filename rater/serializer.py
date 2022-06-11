from rest_framework import serializers
from .models import Profile,Project,Rating

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'fullname', 'profile_picture', 'bio', 'location', 'contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name', 'project_image', 'description', 'technologies_used', 'pub_date', 'link', 'profile', 'user_id')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('design_rating', 'usability_rating', 'creativity_rating', 'content_rating', 'user_id', 'project')