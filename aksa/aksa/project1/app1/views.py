from django.shortcuts import render
from app1.models import*
from app1.form import*

# Create your views here.
def base(request):
    return render(request,'base.html')
def add_item(request):
    s=empform()
    if request.method=='POST':
        s=empform(request.POST)
        if s.is_valid():
            s.save()
            return view_item(request)
    return render(request,'add.html',{'form':s})


def view_item(request):
    d=emp.objects.all()
    context={'data':d}
    return render(request,'view.html',context)

def edit_item(request,p):
    b=emp.objects.get(pk=p)
    form=empform(instance=b)
    if request.method=='POST':
        form=empform(request.POST,instance=b)
        if form.is_valid():
            form.save()
            return view_item(request)
    return render(request,'edit.html',{'form':form})
def delete_item(request,p):
    b=emp.objects.get(pk=p)
    b.delete()
    return view_item(request)
    

        
        