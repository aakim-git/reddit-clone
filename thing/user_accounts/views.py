from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from user_accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# There are custom views.
# function based view
def home(request):
    # you would usually pull these variables from a database. 
    numbers = {1,2,3,4}
    name = "bob BOBBINGTON >:("


    # this implicitely loads the '/template/user_accounts/login.html'
    # you can also pass in a variable list of information.
    args = {'name': name, 'numbers': numbers}
    return render(request, 'user_accounts/home.html', args)

def register(request):
    if request.method == 'GET': #User's first time in the register page
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'user_accounts/register.html', args)

    elif request.method == 'POST': #user is sending info to server
        form = RegistrationForm(request.POST) #request from parameter ; custom form as defined in forms.py
        if form.is_valid(): #kind of the default django requirements
            form.save() #saves into database
            return redirect('/user_accounts/')

def profile(request):
    args = {'user': request.user} #if a user is logged in, we pass in that whole user object (password, email, etc. )
    return render(request, 'user_accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance  = request.user)

        if form.is_valid():
            form.save()
            return redirect('/user_accounts/profile')

    elif request.method == 'GET':
        form = UserChangeForm(instance= request.user)
        args = {'form':form}
        return render(request, 'user_accounts/edit_profile.html', args)










