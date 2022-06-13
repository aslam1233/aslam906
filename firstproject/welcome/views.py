from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from welcome.models import Cars


def fun(request):
    return HttpResponse("This is a welcome page")


def fun1(request):
    return HttpResponse("Hi")


def fun2(request):
    if request.method == 'GET':
        return render(request, 'cars.html')
    else:
        name = request.POST.get('name')
        car = request.POST.get('car')
        cmp = request.POST.get('cmp')
    Cars.objects.create(name=name, car=car, cmp=cmp)
    return render(request, 'cars.html')


def display(request):
    ob = Cars.objects.all()
    return render(request, 'welcome2.html', {'ob': ob})


def delete(request, id):
    Cars.objects.get(id=id).delete()
    ob = Cars.objects.all()
    return render(request, 'welcome2.html', {'ob': ob})

