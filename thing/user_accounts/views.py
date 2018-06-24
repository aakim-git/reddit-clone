from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# function based view
def home(request):
    return HttpResponse('Home Page! D:')
