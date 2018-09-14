"""civilizedTechnologies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from civilized_app.views import IndexView,HomePage,AboutView,jobsPage,DesktopView,DigitalView,WebAppView,ManagementView,MobileView,NetworkingView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('home',HomePage, name='home'),
    path('about/',AboutView.as_view(), name = 'about'),
    path('jobs/',jobsPage, name='jobs'),
    path('management/', ManagementView.as_view(), name='management'),
    path('mobile/', MobileView.as_view(), name='mobile'),
    path('desktop/', DesktopView.as_view(), name='desktop'),
    path('digital/', DigitalView.as_view(), name='digital'),
    path('webapp/', WebAppView.as_view(), name='webapp'),
    path('network/', NetworkingView.as_view(), name='network'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
