from django.shortcuts import render
from bakeryapp.models import Bakery
# Create your views here.

def bakery_list (request):
    bakery_list=Bakery.objects.all()
    context ={'bakery_list':bakery_list}
    return render(request, 'index.html', context)

def about (request):
    return render(request, 'about.html')