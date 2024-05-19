from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    name = "home" 
    return render(request, 'chaiaurdjango/home.html', {'name': home})  

