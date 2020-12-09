from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
from django.http import HttpResponse

def display_topics(request):
    topics=Topic.objects.all()
    return render(request,'display_topic.html',context={'topics':topics})


def display_webpages(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(name='Patricia')
    #webpages=Webpage.objects.get(name='Patricia')
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.all().order_by('-name')
    #webpages=Webpage.objects.all().order_by(Length('name'))
    #webpages=Webpage.objects.all().order_by(Length('name').desc())
    #webpages=Webpage.objects.exclude(topic_name='Music')
    #webpages=Webpage.objects.all()[-1]
    webpages=Webpage.objects.filter(url__startswith='https')
    webpages=Webpage.objects.filter(url__endswith='org/')
    webpages=Webpage.objects.filter(name__contains='a')
    webpages=Webpage.objects.filter(Q(topic_name='Singing') & Q(name='Jacob'))
    webpages=Webpage.objects.filter(Q(topic_name='Singing'))
    webpages=Webpage.objects.filter(Q(name__contains='o') & Q(name__endswith='y') & Q(topic_name='Eating'))
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})

def display_access(request):
    #access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date='1980-01-04')
    #access=Access_Records.objects.filter(date__gte='1980-01-04')
    #access=Access_Records.objects.filter(date__year='1980')
    access=Access_Records.objects.filter(date__month='01')
    access=Access_Records.objects.filter(date__day='23')
    return render(request,'display_access.html',context={'access':access})




def delete_webpage(request):
    Webpage.objects.filter(name='Jacob').delete()
    #return HttpResponse('One row has been deleted Success fully')
    Webpage.objects.all().delete()
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})














