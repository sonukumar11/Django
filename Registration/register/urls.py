from django.urls import path
from . import views
urlpatterns = [
    path('login',views.LoginPage),
    path('register',views.SignupPage),
    path('profile',views.MyProfile)
]
