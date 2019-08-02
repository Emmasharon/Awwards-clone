from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/')
    bio = models.CharField(max_length = 255)
    contact = models.CharField(max_length = 255)
    
    def __str__(self):
        return f'{self.user.username}'
    
class Project(models.Model):
    pic = models.ImageField(upload_to = 'projects/')
    title = models.CharField(blank=True,max_length = 25)
    description = models.CharField(blank=True,max_length = 255)
    link = models.CharField(blank=True,max_length = 10000)
    
    def save_project(self):
        self.save()
        
    def __str__(self):
        return f'{self.profile.user.username}'

