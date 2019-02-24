from django.conf.urls import url
from home.views import home_view, create_post_view, post_view

urlpatterns = [
    url(r'^$', home_view, name = 'home'),
    url(r'^create_post/$', create_post_view, name = 'create_post'),
    url(r'^p/(?P<post_id>[0-9]+)/$', post_view, name = 'post')
    ]


