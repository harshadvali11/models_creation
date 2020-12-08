from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    topics=Topic.objects.all()
    return render(request,'display_topic.html',context={'topics':topics})


def display_webpages(request):
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})