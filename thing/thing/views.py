from django.shortcuts import redirect 
from django.urls import reverse


def home_redirect(request):
    #simple redirect. Home page -> login page.
    return redirect(reverse('user_accounts:home'))
