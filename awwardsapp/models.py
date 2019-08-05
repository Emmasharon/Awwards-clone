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
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
        class Meta:
        ordering = ['-pk']

    def save_project(self):
        self.save()
    
    @classmethod
    def get_project(cls, profile):
        project = Project.objects.filter(Profile__pk = profile)
        return project
    
    @classmethod
    def get_all_projects(cls):
        project = Project.objects.all()
        return project

    @classmethod
    def search_by_profile(cls,search_term):
        projo = cls.objects.filter(profile__name__icontains=search_term)
        return projo

    @classmethod
    def get_profile_projects(cls, profile):
        project = Project.objects.filter(profile__pk = profile)
        return project

    @classmethod
    def find_project_id(cls, id):
        identity = Project.objects.get(pk=id)
        return identity
    
    # def __str__(self):
    #     return f'{self.profile.user.username}'

class Votes(models.Model):
    design = models.CharField(max_length=30)
    usability = models.CharField(max_length=8)
    creativity = models.CharField(max_length=8,blank=True,null=True)
    average = models.FloatField(max_length=8)
    user = models.ForeignKey(User,null = True)
    project = models.ForeignKey(Project,related_name='rate',null=True)


    def __str__(self):
        return self.design

    class Meta:
        ordering = ['-id']

    def save_rate(self):
        self.save()

    @classmethod
    def get_rate(cls, profile):
        rate = Rate.objects.filter(Profile__pk = profile)
        return rate
    
    @classmethod
    def get_all_rating(cls):
        rating = Rate.objects.all()
        return rating