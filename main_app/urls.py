from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/<int:pk>/', views.ShowProfile.as_view(), name="profile"),
    path('profile/<int:pk>/update', views.UpdateProfile.as_view(), name="updateProfile"),
    path('login/', views.Login.as_view(), name="customlogin"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('post/<int:pk>/', views.ShowPost.as_view(), name="post"),
]