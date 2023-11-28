from django.shortcuts import render
from app.models import *
from app.form import *


# Create your views here.

def home(request):
    return render(request,'base.html')
def upload(request):
    form=bookform()
    if(request.method=='POST'):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'add_book.html',{'form':form})

def booklist(request):
    b=Book.objects.all()
    return render(request,'list.html',{'b':b})