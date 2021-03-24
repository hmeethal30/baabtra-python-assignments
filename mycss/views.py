from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def MyCss(request):
    return render(request, 'mycss.html')

def CssAssignment1(request):
    return render(request,'cssassignment1.html')

def CssAssignment2(request):
    return render(request,'cssassignment2.html')