from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Count
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
    #webpages=Webpage.objects.filter(url__startswith='https')
    #webpages=Webpage.objects.filter(url__endswith='org/')
    #webpages=Webpage.objects.filter(name__contains='a')
    #webpages=Webpage.objects.filter(Q(topic_name='Singing') & Q(name='Jacob'))
    #webpages=Webpage.objects.filter(Q(topic_name='Singing'))
    #webpages=Webpage.objects.filter(Q(name__contains='o') & Q(name__endswith='y') & Q(topic_name='Eating'))
    #webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(url__startswith='https')
    #webpages=Webpage.objects.filter(name__length=3)
    #webpages=Webpage.objects.filter(name__in=['Jennifer','Charles'])
    #webpages=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{2}a')

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


def update_webpage(request):
    #Webpage.objects.filter(name='Venky').update(url='https://jennifer_OAR.com/',name='Venky',topic_name='Eating')
    #Webpage.objects.filter(topic_name='Eat').update(name='King Kohli')
    #Webpage.objects.update_or_create(name='Venky',defaults={'url':'https://Venky_OAR.com/'})
    #Webpage.objects.update_or_create(name='King Kohli',defaults={'url':'https://KingKohli.com/'})
    t=Topic.objects.get_or_create(topic_name='Football')[0]
    Webpage.objects.update_or_create(name='Sehwag',defaults={'url':'https://KingKohli.com/','topic_name':t})
    
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})



def form_create_topic(request):
    if request.method=="POST":
        topicname=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=topicname)[0]
        t.save()
        topics=Topic.objects.all()
        return render(request,'display_topic.html',context={'topics':topics})
    return render(request,'form_create_topic.html')



def form_create_webpage(request):
    if request.method=="POST":
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST['url']
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()
        webpages=Webpage.objects.all()
        return render(request,'display_webpage.html',context={'webpages':webpages})
    return render(request,'form_create_webpage.html')



def form_update_webpage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        url=request.POST['url']
        Webpage.objects.filter(name=name).update(url=url)
        webpages=Webpage.objects.all()
        return render(request,'display_webpage.html',context={'webpages':webpages})
    return render(request,'form_update_webpage.html')


def form_delete_webpage(request):
    if request.method=='POST':
        topicname=request.POST['topic']
        Webpage.objects.filter(topic_name=topicname).delete()
        webpages=Webpage.objects.all()
        return render(request,'display_webpage.html',context={'webpages':webpages})
    return render(request,'form_delete_webpage.html')




def select_topic(request):
    topics=Topic.objects.all()
    return render(request,'select_topic.html',context={'topics':topics})



def form_display_webpage(request):
    if request.method=="POST":
        topicname=request.POST.get('topic')
        webpages=Webpage.objects.filter(topic_name=topicname)
        return render(request,'display_webpage.html',context={'webpages':webpages})
    return render(request,'form_display_webpage.html')


def multi_select(request):
    topics=Topic.objects.all()
    if request.method=="POST":
        selected_topics=request.POST.getlist('topic')
        #print(selected_topics)
        webpages=Webpage.objects.none()
        for i in selected_topics:
            webpages=webpages | Webpage.objects.filter(topic_name=i)
        return render(request,'display_webpage.html',context={'webpages':webpages})
    return render(request,'multi_select.html',context={'topics':topics})






def checkbox(request):
    topics=Topic.objects.all()
    return render(request,'checkbox.html',context={'topics':topics})










