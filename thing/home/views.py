from django.shortcuts import render, redirect
from home.forms import HomeForm
from django.urls import reverse
from django.contrib.auth.models import User

from home.models import Post
# Create your views here.
# class-based view
#class home_view(TemplateView):
#   template_name = 'home/home.html'


def home_view(request):
    if request.method == 'GET':
        form = HomeForm()
        posts = Post.objects.all().order_by('created') # retrieves all 'Post' objects from the database. 
        users = User.objects.all()
        args = {'form':form, 'posts':posts, 'users':users}# we now want to pass the Posts to the template 
        return render(request, 'home/home.html', args)

    elif request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #saves all the data in the form into the database. Available bc of ModelForm
            #commit = False bc we haven't fulfilled all the fields in the modelform 'HomeForm'
            post.user = request.user # this is the logged in user. 
            # post has the 'user' variable because the save() returns an empty user field. 
            post.save() #this is the fulfill the remaining 'user' field in HomeForm
            text = form.cleaned_data['post'] #this is the name of the field in the form
            form = HomeForm()
            return redirect(reverse('home:home'))

        args = {'form' : form, 'text':text}
        return render(request, 'home/home.html', args)


