from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyHtml,name= 'myhtml'),
    path('htmlassignment1', views.HtmlAssignment1,name= 'htmlassignment1')

]