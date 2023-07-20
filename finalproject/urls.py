from report.views import *

"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

urlpatterns = [
    path('', register),
    path('basicInformation/', basicInformation, name='basicInformation'),
    path('yearOne/', yearOne, name='yearOne'),
    path('yearTwo/', yearTwo, name='yearTwo'),
    path('yearThree/', yearThree, name='yearThree'),
    path('incomeTaxReturnFiles/', incomeTaxReturnFiles, name='incomeTaxReturnFiles'),
    path('personalFinancialStatementFiles/', personalFinancialStatementFiles, name='personalFinancialStatementFiles'),
    path('finalReport/', finalReport, name='finalReport'),
    path('register/', register, name='register'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('restart/', restart, name='restart'),
]
