from django.urls import path, include
from . import views

urlpatterns = [
    path('myhtml', views.MyHtml,name= 'myhtml')
]