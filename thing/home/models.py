from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key = True, editable = False)

    title = models.CharField(max_length = 100)
    post_content = models.CharField(max_length = 5000)
    link = models.CharField(max_length = 200, default = "")
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add = True) #saves date on creation
    updated = models.DateTimeField(auto_now = True) # saves date on update
    votes = models.ManyToManyField('Vote', related_name = 'vote_list')
    points = models.IntegerField(default = 0)
	
    comments = models.ManyToManyField('Comment', related_name = 'comment_list')
	
class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.PROTECT)
    vote = models.IntegerField(default = 0)
	
class Comment(models.Model):
    comment_text = models.CharField(max_length = 5000)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add = True) 
    updated = models.DateTimeField(auto_now = True) 
    points = models.IntegerField(default = 0)
	


