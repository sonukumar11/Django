from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Users
# Create your views here.

isSignedIn = False
profileInfo = {}

def LoginPage(request):
    valid = True
    if request.method == "POST":
        email = request.POST['mail']
        password = request.POST['Password']
        if len(Users.objects.filter(Email=email,Password=password)) == 1:
            MyUser = Users.objects.filter(Email=email,Password=password)[0]
            print(MyUser.Fullname)
            isSignedIn = True
            print("User Signed In Successfully...")
            profileInfo = {
                "fullname" : MyUser.Fullname,
                "username" : MyUser.Username,
                "email" : MyUser.Email,
                "phoneNumber" : MyUser.PhoneNumber,
                "password": MyUser.Password,
                "gender":MyUser.gender,
                "isSignedIn":isSignedIn
            }
            return render(request,"register/profile.html",profileInfo)
        else:
            valid = False
            print("Enter a Valid Username or Password")
            return render(request,"register/login.html",{
                "valid":valid
            })
    return render(request,"register/login.html",{
        "valid":valid
    })


def SignupPage(request):
    match = False
    new = True
    if request.method == "POST":
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['mail']
        phonenumber = request.POST['phone']
        password = request.POST['Password']
        confirmPassword = request.POST['confirm']
        gender = request.POST['gender']
        print("Full Name : ",fullname)
        print("User Name : ",username)
        print("Email Address: ",email)
        print("Phone Number: ",phonenumber)
        print("Password : ",password)
        print("Confirm Password: ",confirmPassword)
        print("Gender: ",gender)
        if password == confirmPassword:
            if len(Users.objects.filter(Email=email)) == 0:
                Users.objects.create(Fullname=fullname,Username=username,Email=email,PhoneNumber=phonenumber,Password=password,gender=gender)
                print("Registered Successfully....")
                return HttpResponseRedirect('/login')
            else:
                new = False
                return render(request,"register/signup.html",{
                'match':match,
                'new':new
                })
        else:
            match = True
            print("Password and Confirm Password does not Match..")
            return render(request,"register/signup.html",{
                'match':match,
                'new':new
                })
    return render(request,"register/signup.html",{
                'match':match,
                'new':new
                })

def MyProfile(request):
    return render(request,"register/profile.html",profileInfo)