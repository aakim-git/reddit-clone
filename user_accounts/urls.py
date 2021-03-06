from django.conf.urls import url
from . import views #import the view file from the current app
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
        #since these urls belong to the "user_accounts" app, they by default extend from www.asd/user_accounts/...
        #also, at url /user_accounts/ , it will load the "home" object in the views file in this app.
        url(r'^login/$', login, {'template_name': 'user_accounts/login.html'}, name = 'login'),
        #at url .../login, we load the view "login", with our custom template login.html
        url(r'^logout/$', logout, {'template_name': 'user_accounts/logout.html'}, name = 'logout'), #again, the view 'logout' is from the imported library. 
        url(r'^register/$', views.register, name = 'register'),
        url(r'^profile/$', views.profile, name = 'profile'),
        url(r'^profile/(?P<pk>\d+)/$', views.profile, name = 'profile_with_pk'),
        url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile') 
]


