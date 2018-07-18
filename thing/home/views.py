from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class-based view
class home_view(TemplateView):
    template_name = 'home/home.html'
