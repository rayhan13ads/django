from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# index page
class IndexView(TemplateView):
    template_name ='index.html'
#home Page

class Home(TemplateView):
    template_name = "home.html"
