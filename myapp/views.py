from django.forms.forms import Form
from django.http import request
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def welcome(request):
    return render(request, "welcome.html")

def load_from(request):
    form = EmployeeForm
    return render(request, "index.html", {'form': form})
    
def add(request):
    Form = EmployeeForm(request.POST)
    Form.save()
    return redirect('/show')

def show(request):
    employee = Employee.objects.all
    return render (request,'show.html', {'employee': employee})    


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})        

def update (request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show') 

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')

def search(request):
    given_name = request.POST['name']
    employee = Employee.objects.filter(ename__icontains=given_name)
    return render(request, 'show.html', {'employee': employee})