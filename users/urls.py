from django.urls import path
from .import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('profile', views.UserProfile, name="profile"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
]