from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
  return HttpResponse("Hello, welcome to the ecommerce home page!")
