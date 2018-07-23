from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add = True) #saves date on creation
    updated = models.DateTimeField(auto_now = True) # saves date on update

