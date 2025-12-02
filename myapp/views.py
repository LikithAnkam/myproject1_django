from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is Home Page")
    return render(request,"home.html",{"year":2025})

def about(request):
    # return HttpResponse("This is about view page")
    return render(request,"about.html")
def contact(request):
    # return HttpResponse("This is contact page ")
    return render(request,"contact.html")
def login(request):
    # return HttpResponse("This is login page")
    return render(request,"login.html")
def register(request):
    # return HttpResponse("This is register page")
    return render(request,"register.html")


