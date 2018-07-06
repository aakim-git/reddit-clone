from django.contrib import admin
from user_accounts.models import UserProfile

# Register your models here.
admin.site.register(UserProfile) #this allows the model to appear in /admin
