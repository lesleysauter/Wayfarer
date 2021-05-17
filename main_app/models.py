from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

# Create your models here.

class User(Model):

    username = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    current_city = models.CharField(max_length=250)
    join_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Post(Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    content = models.CharField(max_length=10000)

