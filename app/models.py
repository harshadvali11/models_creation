from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField(max_length=150)

    def __str__(self):
        return self.name



class Access_Records(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()



'''
a=Access_Records.objects.get_or_create(name=w,date='02-03-2020')[0]

auto_now=True

date when we have created model   01-12-2020

date when u r inserting the data   02-12-2020

date   02-12-2020

date when u r inserting the data   25-12-2020
        date 25-12-2020




auto_now_add=True

date when we have created model   01-12-2020

date when u r inserting the data   02-12-2020

date   01-12-2020

date when u r inserting the data   25-12-2020

        date 01-12-2020

'''













