from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def MyHtml(request):
    return render(request, 'myhtml.html')