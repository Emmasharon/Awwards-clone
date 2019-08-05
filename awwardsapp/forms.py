from .models import Project,Profile, Votes
from django import forms
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['vote']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude= ['user','project']