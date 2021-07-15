from django.contrib import messages
from django.db import models
from django.db.models.fields import CharField



# Create your models here.
class subscribers(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name+''+self.email

class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=300)
    def __str__(self):
        return self.name+''+self.email+''+self.subject

class Application(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=10)
    email=models.EmailField()
    state=models.CharField(max_length=100) 
    address=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100) 
    location=models.CharField(max_length=100)
    skills=models.CharField(max_length=100) 
    textarea=models.CharField(max_length=100)

    def __str__(self):
         return self.firstname + ''+self.lastname+ ''+self.phonenumber+ ''+self.email+ ''+self.state+ ''+self.address+ ''+self.Gender+ ''+self.location+ ''+self.skills+ ''+self.textarea

