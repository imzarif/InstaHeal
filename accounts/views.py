from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def signup(request):
    if request.method=='POST':
        if request.POST['pass']==request.POST['cpass']:
           try:
               user = User.objects.get(username=request.POST['email'])
               return render(request, 'accounts/signup.html', {'error':'This email has already been used'})
           except User.DoesNotExist:
               user = User.objects.create_user(request.POST['email'],email=request.POST['phone'],first_name=request.POST['name'], password=request.POST['pass'])
               auth.login(request,user)
               return redirect('home')

        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'email or password does not match'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
        if request.method == 'POST':
            auth.logout(request)
            return redirect('home')




