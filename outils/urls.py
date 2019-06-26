# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:25:26 2019

@author: Utilisateur
"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('beginner',views.beginner, name='beginner'),
    path('results',views.results, name='results'),
    path('home',views.home,name='home'),
    path('master',views.master,name='master'),
    path('level',views.level,name='level'),
]