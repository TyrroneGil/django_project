from django.shortcuts import render
from django.http import JsonResponse
dictionary = {
    "message":['Tyrrone','Gil','Azusano']
}

# Create your views here.
def renderIndex(request):
    return render('','index.html',{"message":"Hello World"})
    
def renderAbout(request):
    return render(request,'about.html')