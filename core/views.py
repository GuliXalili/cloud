from django.shortcuts import render
from .models import *
def party(request):
    part = Party.objects.all()
    context ={
        'part': part
    }
    return render(request, 'index.html', context)
