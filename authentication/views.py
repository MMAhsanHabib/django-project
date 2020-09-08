from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib import messages

def authlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username = name, password = password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request,'Invalid uswername or password')

    return render(request,'login.html')


def authregister(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username Already Exist')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'Email Already Exist')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                return redirect('login')
        else:
            messages.error(request,'Password not matched')



    return render(request,'register.html')





def forgotpassword(request):
    return render(request,'forgotpassword.html')


def authlogout(request):
    logout(request)
    messages.success(request,'Successfully logout')
    return redirect('login')




