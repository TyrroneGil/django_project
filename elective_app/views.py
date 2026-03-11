from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Students
# Create your views here.
def renderIndex(request):
    students = Students.objects.all()
    return render(request,'index.html',{'students':students})

def renderUpdatewithDetails(request,id):
    student = Students.objects.get(id=id)
    return render(request,'update.html',{"student":student})

def addStudent(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        course = request.POST['course']
        year = int(request.POST['year'])
        Students.objects.create(fullname=fullname,course=course,year=year)
    return redirect('/')
def deleteStudent(request,id):
    if request.method == "GET":
        Students.objects.filter(id=id).delete()
        return redirect('/')

def updateStudent(request):
    if request.method == "POST":
        id = request.POST['id']
        fullname = request.POST['fullname']
        course = request.POST['course']
        year = int(request.POST['year'])
        Students.objects.filter(id=id).update(fullname=fullname,course=course,year=year)
        return redirect('/')
    else:   
        return JsonResponse({'message':"Invalid Request"})