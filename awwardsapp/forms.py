from .models import Project,Profile, Votes
from django import forms
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'pub_date', 'profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','vote']

class VoteForm(forms.ModelForm):
    class Meta:
        model =Rate
        exclude= ['user','project']