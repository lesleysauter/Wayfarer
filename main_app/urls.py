from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('login/', views.Login.as_view(), name="customlogin"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('post/<int:id>/', views.Post.as_view(), name="post"),
]