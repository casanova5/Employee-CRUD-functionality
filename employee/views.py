from django.shortcuts import render, redirect
from .models import employee
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializer import employeeSerializer

# Create your views here.
def insertform(request):
    context = {}
    return render(request, 'insertform.html', context)

def insert(request):
    emp = employee()
    emp.firstname = request.POST['fname']
    emp.lastname = request.POST['lname']
    emp.employeeid = request.POST['emp_id']
    emp.save()
    return redirect('getall')

def getall(request):
    employee1 = employee.objects.all()
    serializer = employeeSerializer(employee1, many=True)
    context = {"data": serializer.data}
    return render(request, 'loginsuccessful.html', context)

def updateform(request):
    context = {}
    return render(request,'updateform.html', context)

def updatecheck(request):
    emp = employee.objects.get(employeeid = request.POST['eid'])
    if emp is not None:
        context = {
            'employeeid': emp.employeeid,
            'fname': emp.firstname,
            'lname':emp.lastname,
        }
        return render(request, 'updatecheckform.html', context)
    else:
        return render(request, 'updateform.html', {'error':'Emplyee id doesnot exist'})

def update(request):
    emp = employee.objects.get(employeeid=request.POST['emp_id'])
    emp.firstname = request.POST['fname']
    emp.lastname = request.POST['lname']
    emp.employeeid = request.POST['emp_id']
    emp.save()
    return redirect('getall')


def deleteform(request):
    context = {}
    return render(request, 'deleteform.html', context)

def deletecheck(request):
    emp = employee.objects.get(employeeid=request.POST['eid'])
    if emp is not None:
        context = {
            'employeeid': emp.employeeid,
            'fname': emp.firstname,
            'lname':emp.lastname,
        }
        return render(request, 'deletecheckform.html', context)
    else:
        return render(request, 'deleteform.html', {'error':'Emplyee id doesnot exist'})

def delete(request):
    emp = employee.objects.get(employeeid=request.POST['emp_id'])
    return redirect('getall')

