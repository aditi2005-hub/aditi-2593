from django.contrib import admin
from django.urls import path, include

from Djangodtwo import views

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('page1/',views.page1),
    path('page2/',views.page2),
    path('page4/',views.page4),
    path('page5/',views.page5),
    path('page6/',views.page6),
    path('page7/',views.page7),
    path('page3/',views.page3),


]