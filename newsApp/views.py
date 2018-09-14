from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from django.http import HttpResponse
from django.conf import settings
from .models import BlogModel

# Create your views here.

class NewsDetails(DetailView):
    queryset = BlogModel.objects.all()
    template_name='news/newsDetails.html'

    
    def get_context_data(self, **kwargs):
        context = super(NewsDetails, self).get_context_data(**kwargs)
        return context
    


class NewsList(ListView):
    queryset = BlogModel.objects.all()
    template_name='news/list.html'


    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        return context
    