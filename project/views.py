from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from .models import automate
from .models import register_details
def index(request):
    if request.method=="GET":
        return render (request,'index.html')
    elif request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        exam = request.POST.get('exam')
        
        # Create a new instance of RegisterDetails model and save the data
        new_detail = register_details.objects.create(name=name, email=email, exam=exam)
        new_detail.save()
        send_mail('Government Exam Registration',exam+" successfully registered",'rasheq53@gmail.com',[email],fail_silently=False)
        return render (request,'index.html')


def web1(request):
    if request.method=="GET":
        data=automate.objects.all()
        return render (request,'web1.html',{'data':data})