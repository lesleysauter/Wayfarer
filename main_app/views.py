from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, response
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserCreationForm()
        return context


class ShowProfile(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        context = {"user": user, "posts": Post.objects.filter(profile=user.profile)}
        return render(request, "profile.html", context)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Profile, self).for_valid(form)

class UpdateProfile(View):
    def post(self, request, pk):
        profile = Profile.objects.get(user=pk)
        profile.name = request.POST["name"]
        profile.current_city = request.POST["city"]
        profile.save()
        return redirect(f"/profile/{pk}")
    

class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f"/profile/{user.pk}")
        
        else:
            return HttpResponse("Unable to login!", content_type="text/plain")


class Signup(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(
                user=request.user, 
                name="New User", 
                current_city="Current City"
                )
            return redirect(f"/profile/{user.pk}")
        else:
            return HttpResponse("Unable to create profile!", content_type="text/plain")


class ShowPost(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {"post": post}
        return render(request, "show-post.html", context)