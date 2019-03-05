from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

from home.models import Post, Vote, Comment
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
            post_content =  form.cleaned_data['post_content']
            post.save()
            return redirect(reverse('home:home'))
			
			
def post_view(request, post_id):
    target_post = Post.objects.get(post_id = post_id)
	# user submitted a comment
    if(request.method == 'POST'):
        new_comment = Comment(author = request.user, comment_text = request.POST['text'])
        new_comment.save()
        target_post.comments.add(new_comment)
		
		
    vote = 0
	
    find_vote = target_post.votes.all().filter(voter = request.user)
    if len(find_vote) > 0:
	    vote = find_vote[0].vote
		
    args = {'post':target_post, 'submit_comment_form':submit_comment_form(), 'cur_user':request.user.id, 'vote': vote, 'comments':target_post.comments.all()}
    return render(request, 'home/post.html', args)
	
def post_vote(request):
    if request.method == 'POST':
        target_post = Post.objects.get(post_id = request.POST['id'])
        target_post.points += int(request.POST['change'])
        cur_vote = target_post.votes.filter(voter = request.user)
		
        if len(cur_vote) == 0:
            new_vote = Vote(voter = request.user, vote = request.POST['change'])
            new_vote.save()
            target_post.votes.add(new_vote)
			
        else:
            cur_vote[0].vote = request.POST['change']
            cur_vote[0].save()
        
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
	
	
	
	
	


