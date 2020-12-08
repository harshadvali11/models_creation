# population of data into models
# creating django environmant

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project12.settings')
#addding django features
import django
django.setup()
from app.models import *
from faker import Faker
f=Faker()
import random
topics=['Cricket','Eating','Singing','Music']

def add_topics():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def add_webpages(webpagename,url):
    topic_name=add_topics()
    w=Webpage.objects.get_or_create(topic_name=topic_name,name=webpagename,url=url)[0]
    w.save()
    return w

def add_records(webpagename,url,date):
    name=add_webpages(webpagename,url)
    a=Access_Records.objects.get_or_create(name=name,date=date)[0]
    a.save()



def add_data(n):
    for i in range(n):
        fakename=f.first_name()
        fakeurl=f.url()
        fakedate=f.date()
        add_records(fakename,fakeurl,fakedate)


if __name__=='__main__':
    print('population of data hass started')
    n=int(input('enter number of records to insert'))
    add_data(n)
    print('Successfully inserted the data')




































