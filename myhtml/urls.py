from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyHtml,name= 'myhtml'),
    path('htmlassignment1', views.HtmlAssignment1,name= 'htmlassignment1'),
    path('htmlassignment2', views.HtmlAssignment2,name= 'htmlassignment2'),
    path('htmlassignment3', views.HtmlAssignment3,name= 'htmlassignment3'),
]