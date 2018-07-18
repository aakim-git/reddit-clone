from django.db import models
from django.contrib.auth.models import User # the default django user model. 
from django.db.models.signals import post_save 

# Create your models here.
class UserProfile(models.Model):
    #once you create a model here, you have to "Register" it at admin.py
    #then, you makemigrations
    user = models.OneToOneField(User)
    description = models.CharField(max_length = 100, default = '')
    city = models.CharField(max_length = 100, default = '')
    email = models.URLField(default = '')
    phone = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username

# whenever we create a "User", a "UserProfile" is also created
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender = User)




