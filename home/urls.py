from django.conf.urls import url
from home.views import home_view, create_post_view, post_view, post_vote

urlpatterns = [
    url(r'^$', home_view, name = 'home'),
    url(r'^create_post/$', create_post_view, name = 'create_post'),
    url(r'^p/(?P<post_id>[0-9]+)/$', post_view, name = 'post'),
	url(r'^post_vote/$', post_vote, name = 'post_vote')
    ]


