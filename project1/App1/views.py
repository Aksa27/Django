from django.shortcuts import render
from django.http import HttpResponse
from App1.models import students,employee
# Create your views here.
 
def home(request):
    #d={'name':'Alex','age':'20'}
    d=students.objects.all()
    return render(request,'home.html',{'t':d})

 
def index(request):
    return HttpResponse("hello welcome to page ")

def employee2(request):
    #d={'name':'Alex','age':'20'}
    d=employee.objects.all()
    return render(request,'data.html',{'t':d})

 