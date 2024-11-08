from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Student

from  django.db.models import Q

from .forms import StudentInfoForm
# Create your views here.

def list_student(request):
    student=Student.objects.all()
    return render(request,'crud/list_student.html',{'student':student})

def update_student(request,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        fm=StudentInfoForm(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")
    else:
        student=Student.objects.get(pk=id)
        fm=StudentInfoForm(instance=student)
    return render (request, "crud/update_student.html",{'form':fm})


def deletedata(request ,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect("/")

def add_student(request ):
    if request.method=="POST":
        fm=StudentInfoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else :
        fm=StudentInfoForm()
    return render(request,'crud/add.html',{'form':fm})


def searchstudent(request):
    if request.method == 'POST':
        n1 = request.POST.get('output')
        student = Student.objects.all()
        std = None  # Initialize the variable
        if n1:
            std = student.filter(
                Q(firstname__icontains=n1) |
                Q(lastname__icontains=n1) |
                Q(email__icontains=n1) |
                Q(phone__icontains=n1) |
                Q(branch__icontains=n1)
            )

        return render(request, "crud/list_student.html", {'student': std})
    else:
        return HttpResponse('An Exception Occurred')


