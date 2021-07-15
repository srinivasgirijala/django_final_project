
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.urls import reverse_lazy
from information.forms import SignUpForm
from django.views.generic import CreateView
from django.views.generic import TemplateView


from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.

from information.models import Application,feedback,subscribers


class HomeView(TemplateView):
    template_name='security/home.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'security/register.html'



@login_required(login_url='/')
def dashboard(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        user=subscribers(name=name,email=email)
        user.save()
        messages.success(request,request.POST['name'])
        return redirect('dashboard')
    else: 
       return render(request,'security/dashboard.html')




def About(request):
    return render(request,'security/About.html')



def contact(request):
  if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        user=feedback(name=name,email=email,subject=subject)
        user.save()
        messages.success(request,request.POST['name']+"")
        return redirect('dashboard')
  else:
     return render(request,'security/contact.html')

 

def careers(request):
     if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        state=request.POST['state']
        address=request.POST['address']
        Gender=request.POST['Gender']
        location=request.POST['location']
        skills=request.POST['skills']
        textarea=request.POST['textarea']
        user=Application(firstname=firstname,lastname=lastname,phonenumber=phonenumber,email=email,state=state,address=address,Gender=Gender,location=location,skills=skills,textarea=textarea)
        user.save()
        return redirect('dashboard')
     else:
       return render(request,'security/careers.html')


   




def created(request):
    return render(request,'security/created.html')

def become(request):
    return render(request,'security/become.html')

def technologies(request):
    return render(request,'security/technologies.html')

def training(request):
    return render(request,'security/training.html')

