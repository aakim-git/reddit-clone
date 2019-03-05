import re

from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLS = []
for url in settings.LOGIN_EXEMPT_URLS:
    EXEMPT_URLS += [re.compile(url)]

# Redirects certain pages to login page if needed 
class LoginRequiredMiddleware:
    # This function is always required
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__ (self, request):
        response = self.get_response(request)
        return response

    # This is called whenever a view is loaded. 
    def process_view(self,request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')

        path = request.path_info.lstrip('/')
        print(path)
        # if the user is not logged in
        if not request.user.is_authenticated:
            exempt = 0
            for url in EXEMPT_URLS:
                if url.match(path):
                    exempt = 1

            if exempt == 0:
                return redirect(settings.LOGIN_URL)
           
          





        
