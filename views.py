from django.shortcuts import render
from django.http import request
def welcome(request):
    return render(request, "welcome.html")