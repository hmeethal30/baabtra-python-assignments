from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def MyHtml(request):
    return render(request, 'myhtml.html')

def HtmlAssignment1(request):
    # return render(request, 'assignment1.html')    
    return render(request, 'htmlassignment1.html')

def HtmlAssignment2(request):
    return render(request,'htmlassignment2.html')

def HtmlAssignment3(request):
    return render(request,'htmlassignment3.html')
