from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
  return HttpResponse("this is home page")

def about(request):
  return HttpResponse("this is about page")

def contact(request):
  return HttpResponse("this is contact page")

def page1(request):
  return HttpResponse("this is page1 page")

def page2(request):
  return HttpResponse("this is page2 page")

def page3(request):
  return HttpResponse("this is page3 page")

def page4(request):
  return HttpResponse("this is page4 page")

def page5(request):
  return HttpResponse("this is page5 page")

def page6(request):
  return HttpResponse("this is page6 page")

def page7(request):
  return HttpResponse("this is page7 page")