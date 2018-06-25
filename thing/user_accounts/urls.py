from django.conf.urls import url
from . import views #import the view file in the current app


urlpatterns = [
	url(r'^$', views.home),
        #since these urls belong to the "user_accounts" app, they by default extend from www.asd/user_accounts/...
        #also, at url /user_accounts/ , it will load the "home" object in the views file in this app. 
]

