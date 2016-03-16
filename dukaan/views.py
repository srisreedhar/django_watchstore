from django.shortcuts import render
from django.http import HttpRequest  # optional import

# created a view for store-index page

def index(request):
    return render(request,"index.html")

# creating a view for dukaan

def dukaanam(request):
    return render(request, "dukaan.html")


# def registration(request):
#     return render(request)



