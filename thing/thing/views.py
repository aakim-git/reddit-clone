from django.shortcuts import redirect 
from django.urls import reverse


def login_redirect(request):
    #simple redirect. Home page -> login page.
    return redirect('/user_accounts/')
