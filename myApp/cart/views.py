from django.shortcuts import render

from django.http import HttpResponse
def election(request):
    return HttpResponse("<h2>This is the election page<h2>")

def contactUs(request):
    return HttpResponse("<h2>This is the contact Us page</h2>")

def Register(request):
    return HttpResponse("<h2> This is the Register Page</h2>")
