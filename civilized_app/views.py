from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
# Create your views here.

# index page
class IndexView(TemplateView):
    template_name ='index.html'
    
#home Page
def HomePage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(request.POST)
        # email system
        subject = 'Contact form receved'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rayhan13ads@gmail.com',]
        #message
        contact_message = "{0}\n,==> from {1} with email {2}".format(message,name,email)
    
        send_mail(subject,contact_message,email_from,recipient_list,fail_silently=True)
        #return redirect('')
    return render(request , "home.html",{})
#About Page

class AboutView(TemplateView):
    template_name="about.html"

class JobsView(TemplateView):
    template_name = "jobs.html"

class DesktopView(TemplateView):
    template_name = "desktop.html"

class MobileView(TemplateView):
    template_name = "mobileapplication.html"

class DigitalView(TemplateView):
    template_name = "digital.html"

class WebAppView(TemplateView):
    template_name = "webapplication.html"

class ManagementView(TemplateView):
    template_name = "management.html"


class NetworkingView(TemplateView):
    template_name = "network.html"





