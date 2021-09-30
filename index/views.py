from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import about,slider,featuredservices, services, clients, portfolio, testimonial, contactlist, contactform
from django.core.mail import send_mail

def home(request):
    contactlistdata = contactlist.objects.all()[0]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(
            email ,
            message,
            email,
            ['ishaan18nagpal@gmail.com']
            )

        contactformdata = contactform(name=name, email=email, subject=subject, message=message)
        contactformdata.save()


    context = {
        'contactlist':contactlistdata,
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')

def team(request):
    return render(request,'team.html')

def testimonials(request):
    return render(request,'testimonials.html')

def services(request):
    return render(request,'services.html')

def cremation(request):
    return render(request,'cremation.html')

def termsofservice(request):
    return render(request,'termsofservice.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')
