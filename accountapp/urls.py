from django.contrib import admin
from django.urls import path,include
from accountapp import views

urlpatterns = [
    path('',views.hi),
]
