from django.db import models
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic import CreateView

# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url="/profiles"

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html",{
#             "form":form
#         })

#     def post(self, request):
#         profile = UserProfile(image=request.FILES["user_image"])
#         profile.save()
#         # print(request.FILES["image"])
#         submitted_form = ProfileForm(request.POST , request.FILES)
#         if submitted_form.is_valid():
#             return HttpResponseRedirect('/profiles')
#         return render(request,"profiles/create_profile.html",{
#             "form":submitted_form
#         })
        
class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"
    
