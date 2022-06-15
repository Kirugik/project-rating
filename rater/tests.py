from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.new_user = User(username='robert')
        self.new_user.save() 
        self.new_user_profile = Profile(user = self.new_user, fullname = 'Robert Kirui', bio='Learning software development', location = 'Nairobi', contact = 'robert.kirui@student.moringaschool.com')

    def tearDown(self):
        User.objects.all().delete() 
        Profile.objects.all().delete()


    def test_instance(self):
        '''
        test profile object initialization 
        '''
        self.assertTrue(isinstance(self.new_user_profile, Profile))
        


    def test_save_profile(self):
        '''
        test save profile 
        '''
        self.new_user_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


class ProjectTest(TestCase):
    def setUp(self):
        self.new_user = User(username='robert')
        self.new_user.save_profile()
        self.new_user_profile = Profile(user = self.new_user, fullname = 'Robert Kirui', bio='Learning software development', location = 'Nairobi', contact = 'robert.kirui@student.moringaschool.com')
        self.new_user_profile.save()
        self.new_project = Project(profile = self.new_user, project_name='myproject', description='This is my first project', technologies_used = 'python', link='www.mynewproject.com')

    
    def tearDown(self):
        User.objects.all().delete() 
        Profile.objects.all().delete()
        Project.objects.all().delete() 


    def test_instance(self):
        '''
        test project object initialization
        '''
        self.assertTrue(isinstance(self.new_project, Project))


    def test_save_project(self):
        '''
        test save project 
        '''
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_search(self):
        '''
        test search method for project search method
        '''
        self.new_project.save_project()
        keyword='quotes'
        found_projects = Project.search_project(keyword)
        self.assertTrue(len(found_projects) > 0 ) 
