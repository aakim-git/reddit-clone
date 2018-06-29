from django.conf.urls import url
from . import views #import the view file in the current app
from django.contrib.auth.views import login # login library

urlpatterns = [
	url(r'^$', views.home),
        #since these urls belong to the "user_accounts" app, they by default extend from www.asd/user_accounts/...
        #also, at url /user_accounts/ , it will load the "home" object in the views file in this app.
        url(r'^login/$', login, {'template_name': 'user_accounts/login.html'})
        #at url .../login, we load the view "login", with our custom template login.html
]


