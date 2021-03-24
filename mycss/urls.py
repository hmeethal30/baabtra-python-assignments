from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyCss,name= 'mycss'),
    
    path('cssassignment1', views.CssAssignment1,name= 'cssassignment1'),
    path('cssassignment2', views.CssAssignment2,name= 'cssassignment2'),




]