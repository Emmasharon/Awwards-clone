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

def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day

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
@login_required(login_url='/accounts/login')

def post_project(request):
    if request.method == 'POST':
        projectform = ProjectForm(request.POST, request.FILES)
        if projectform.is_valid():
            post = projectform.save(commit=False)
            post.profile = request.user.profile
            post.save()
            return redirect('index.html')
    else:
projectform = ProjectForm()
    return render(request,'update-project.html',locals())

def view_project(request):
    project = Project.objects.get_all()
    return render(request,'index.html', locals())