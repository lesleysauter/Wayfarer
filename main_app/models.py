from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

# Create your models here.

class Profile(Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    current_city = models.CharField(max_length=250)
    join_date = models.DateTimeField(auto_now_add=True)
    

class Post(Model):

    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    content = models.TextField(max_length=10000)