from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
def home(request):
    return HttpResponse("<h2>Hello This is My First django Project application<h2>")

def aboutUs(request):
    return HttpResponse("<h2>This is the about us page</h2>")

def loginPage(request):
    return HttpResponse("<h2> This is the login Page</h2>")


