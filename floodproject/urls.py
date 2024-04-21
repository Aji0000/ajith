"""
URL configuration for floodproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from floodapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.userregister,name='register'),
    path('login',views.userlogin,name='login'),
    path('logout',views.userlogout,name='logout'),
    path('prediction',views.prediction,name='prediction'),
    path('profile',views.profile,name='profile'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('prevention',views.prevention,name='prevention'),
    path('reliefcamps',views.reliefcamps,name='reliefcamps'),
    path('floods',views.floods,name='floods'),
    path('presentprediction',views.presentprediction,name='presentprediction'),
]
