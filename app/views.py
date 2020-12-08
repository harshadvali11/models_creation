from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def display_topics(request):
    topics=Topic.objects.all()
    return render(request,'display_topic.html',context={'topics':topics})


def display_webpages(request):
    #webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(name='Patricia')
    #webpages=Webpage.objects.get(name='Patricia')
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.all().order_by('-name')
    #webpages=Webpage.objects.all().order_by(Length('name'))
    #webpages=Webpage.objects.all().order_by(Length('name').desc())
    webpages=Webpage.objects.exclude(topic_name='Music')
    webpages=Webpage.objects.all()[-1]
    
    
    return render(request,'display_webpage.html',context={'webpages':webpages})

def display_access(request):
    #access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date='1980-01-04')
    #access=Access_Records.objects.filter(date__gte='1980-01-04')
    #access=Access_Records.objects.filter(date__year='1980')
    access=Access_Records.objects.filter(date__month='01')
    access=Access_Records.objects.filter(date__day='23')
    return render(request,'display_access.html',context={'access':access})



















