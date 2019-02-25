from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

from home.models import Post, Vote
from home.forms import create_post_form, submit_comment_form



def home_view(request):
    posts = getPosts(request, 0)
    users = User.objects.exclude(id=request.user.id)
	
    args = {'posts':posts, 'users':users, 'cur_user':request.user.id}
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
    args = {'post':target_post, 'submit_comment_form':submit_comment_form(), 'cur_user':request.user.id}
    return render(request, 'home/post.html', args)
	
def post_vote(request):
    if request.method == 'POST':
        target_post = Post.objects.get(post_id = request.POST['id'])
        target_post.points += int(request.POST['change'])
		
        new_vote = Vote(voter = request.user, vote = request.POST['change'])
        new_vote.save()
        target_post.votes.add(new_vote)
		
        target_post.save()
        return HttpResponse("Cool")		
		
		
    else:
        return HttpResponse("Error")


def getPosts(request, page_num):
    num_posts = 10
    posts = Post.objects.all().order_by('-created')[page_num*num_posts : page_num*num_posts + num_posts]
	
    votes = []
    for i in range(len(posts)):
        vote = posts[i].votes.all().filter(voter = request.user)
        if(len(vote) == 0):
            votes += [0]
			
        else:
            votes += [vote[0].vote]
    
    return zip(posts,votes)
	
	
	
	
	


