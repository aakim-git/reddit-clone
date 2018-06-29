from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# function based view
def home(request):
    # you would usually pull these variables from a database. 
    numbers = {1,2,3,4}
    name = "bob BOBBINGTON >:("


    # this implicitely loads the '/template/user_accounts/login.html'
    # you can also pass in a variable list of information.
    args = {'name': name, 'numbers': numbers}
    return render(request, 'user_accounts/home.html', args) 
