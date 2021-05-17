from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, response
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class Profile(TemplateView):
    template_name = "profile.html"


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile')
    else:
        return HttpResponse("Unable to log in!", content_type="text/plain")
        
