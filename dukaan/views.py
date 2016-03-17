from django.shortcuts import render
from django.http import HttpRequest  # optional import
from .models import Watch
# created a view for store-index page

def index(request):
    return render(request,"index.html")

# creating a view for dukaan

# create a view for stock and populate the stuff from models.py

def stock(request):
    count = Watch.objects.all().count()
    total_count = Watch.objects.all()

    context = {
        'count': count,
        'totalcount' : total_count,
        'title' : "This is stock views page",
        'Fossil' : total_count[0],
        'second' : total_count[1],
        'third' : total_count[2],
        'fourth' : total_count[3],
    }
    return render(request, 'stock.html',context)

# View for dukaanam

def dukaanam(request):
    return render(request, "dukaan.html")


# def registration(request):
#     return render(request)



