from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
# from .models import Profile,Post,Following,Comment,User
from .forms import ProfileForm,PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# from django.db.models import F

# Create your views here.
def index(request):
    return render(request, 'index.html')