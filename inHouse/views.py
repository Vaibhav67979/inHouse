from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        print(request)
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        logname = request.POST['logname']
        logemail = request.POST['logemail']
        logpass = request.POST['logpass']

        # check for erroneous inputs
        if not logname.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('Login')

        # create user
        myuser = User.objects.create_user(logname, logemail, logpass)
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home/')

    else:
        return HttpResponse('404 - not found')


def handleLogin(request):
    if request.method == 'POST':
        loginname = request.POST['loginname']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginname, password=loginpass)

        if user is not None:
            login(request)
            messages.success(request, "Successfully logged in!")
            return redirect('home/homepage')
        else:
            messages.error(request, "Invalid credentials, please try again!")
            t = {'data': 'Invalid credentials, please try again!'}
            return render(request, 'login.html', t)

    return HttpResponse('404 - not found')
