from django.urls import path, include
from . import views

urlpatterns = [
    path('myhtml', views.MyHtml,name= 'myhtml')
    path('assignment1', views.HtmlAssignment1,name= 'assignment1')

]