from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile,Project
# from .forms import ProfileForm,PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import F

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    def profile(request):
        current_user = request.user
        if request.method == 'POST':
            profileform = ProfileForm(request.POST, request.FILES)
            if profileform.is_valid():
                profile = profileform.save(commit=False)
                profile.user = current_user
                profile.save()
                
            return redirect('profile')

        else:
            profileform = ProfileForm()
            
        return render(request, 'profile.html',locals())
       