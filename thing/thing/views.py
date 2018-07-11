from django.shortcuts import redirect 

def login_redirect(request):
    #simple redirect. Home page -> login page. 
    return redirect('/user_accounts/')
