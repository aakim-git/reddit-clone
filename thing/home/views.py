from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User

from home.models import Post
from home.forms import create_post_form, submit_comment_form


def home_view(request):
	posts = Post.objects.all().order_by('-created')[:10]
	users = User.objects.exclude(id=request.user.id)
	args = {'posts':posts, 'users':users}
	return render(request, 'home/home.html', args)
		
		
def create_post_view(request):
    if request.method == 'GET':
        args = {'create_post_form': create_post_form()}
        return render(request, 'home/create_post.html', args)

    elif request.method == 'POST':
        form = create_post_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False) 
            post.user = request.user 
            post.save()
            post_content = form.cleaned_data['post'] 
            return redirect(reverse('home:home'))
			
			
def post_view(request, post_id):
    target_post = Post.objects.all().filter(post_id = post_id)[0]
    args = {'post':target_post, 'submit_comment_form':submit_comment_form()}
    return render(request, 'home/post.html', args)




