from django.shortcuts import render
from django.http import HttpResponse
from .models import site
# Create your views here.
def home_page(request):
    posts=site.objects.all()
    return render(request,"index.html",{'posts':posts})



