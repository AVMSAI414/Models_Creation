from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_name=models.CharField(max_length=20,primary_key=True)
    
class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    url=models.URLField()
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=21)
    date=models.DateField()
    
