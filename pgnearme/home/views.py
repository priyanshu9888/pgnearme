from django.http.response import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.

def index(request):
    return render(request, 'home/index.html')
def home(request):
        return render(request, 'home/index.html')
# def about(request):
#     return render (request,about.html)
def contact(request):
    return render (request,'contact/index.html')
# def home(request):
#     return render (request,home.html)