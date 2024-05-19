from django.shortcuts import render

def al_chai(request):
    return render(request, 'all_chai.html')