from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyCss,name= 'mycss'),
    
    #css urls
    path('cssassignment1', views.CssAssignment1,name= 'cssassignment1')




]