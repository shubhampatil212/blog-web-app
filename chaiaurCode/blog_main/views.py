from django.http import  HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, This is home")
    return render(request, 'website/home.html')

def about(request):
    return HttpResponse("Hello, This is about")

def contact(request):
    return HttpResponse("Hello, This is contact")