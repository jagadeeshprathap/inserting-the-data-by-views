from django.shortcuts import render

# Create your views here.
from app.models import *

def display(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}

    return render(request,'display.html',context=d)

def display1(request):
    WOT=Webpage.objects.all()
    d={'obj':WOT}

    return render(request,'display1.html',context=d)
def display2(request):
    AOT=AccessRecords.objects.all()
    d={'access':AOT}

    return render(request,'display2.html',context=d)