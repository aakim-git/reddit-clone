from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm #default django registraction form. 

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
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'user_accounts/register.html', args)

    elif request.method == 'POST': #user is sending info to server
        form = UserCreationForm(request.POST) #this is the request in the parameter
        if form.is_valid(): #kind of the default django requirements
            form.save() #saves into database
            return redirect('/user_accounts/')
