from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# function based view
def home(request):
    return render(request, 'user_accounts/login.html') #this implicitely loads the '/template/user_accounts/login.html'
