from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST.get('username')
        # username = request.POST['username']
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        emailAddress = request.POST.get('emailAddress')
        newPassword = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        myUser = User.objects.create_user(username, emailAddress, newPassword)
        myUser.first_name = firstName
        myUser.last_name = lastName
        myUser.save()

        messages.success(request, "Your account has been successfully created!")

        return redirect(signin)
    
    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html", {'firstName':user.first_name})
        else:
            messages.error(request, "Bad credentials!")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out succesfully")

    return redirect('home')
    # return render(request, "authentication/signout.html")