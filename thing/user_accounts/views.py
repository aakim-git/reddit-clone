from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from user_accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.urls import reverse

def home(request):
    args = {}
    return render(request, 'user_accounts/home.html', args)



def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'user_accounts/register.html', args)

    elif request.method == 'POST': 
        form = RegistrationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect(reverse('home:home'))
			
        else:
            return HttpResponse('Error ?')



def profile(request, pk = None): #pk's default value makes it optional
    if pk:
        user = User.objects.get(pk = pk) #retrieves from database that matches primary key. 

    else:
        user = request.user #this is refers to the logged in user. 

    args = {'user': user, 'cur_user':pk} #if a user is logged in, we pass in that whole user object (password, email, etc. )
    return render(request, 'user_accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance  = request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('user_accounts:profile'))

    elif request.method == 'GET':
        form = EditProfileForm(instance= request.user)
        args = {'form':form}
        return render(request, 'user_accounts/edit_profile.html', args)










