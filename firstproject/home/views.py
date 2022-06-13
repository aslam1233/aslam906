from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from home.form import StudentForm
from home.models import Student


def myfun(request):
    return HttpResponse("Welcome to my home page")


def fun1(request):
    return HttpResponse("This is my first project")


def fun2(request):
    return render(request, 'shaheer.html')


def fun3(request):
    if request.method == 'GET':
        return render(request, 'inserting.html')
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
    Student.objects.create(name=name, age=age, dob=dob)
    return render(request, 'inserting.html')


def display(request):
    ob = Student.objects.all()
    return render(request, 'display.html', {'ob': ob})


def delete(request, id):
    Student.objects.get(id=id).delete()
    ob = Student.objects.all()
    return render(request, 'display.html', {'ob': ob})


def insert(request):
    if request.method == 'GET':
        ob = StudentForm()
        return render(request, 'forminsert.html', {'ob': ob})
    else:
        f = StudentForm(request.POST)
        if f.is_valid():
            f.save()
    return redirect('home:display')


def edit(request, id):
    if request.method == "GET":
        ob = Student.objects.get(id=id)
        return render(request, 'edit.html', {'ob': ob})
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
    Student.objects.filter(id=id).update(name=name, age=age, dob=dob)
    return render(request, 'inserting.html')
