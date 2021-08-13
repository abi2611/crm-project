from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
@login_required()
def example(request):
    return render(request,'home.html')    
