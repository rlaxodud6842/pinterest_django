from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hi(request):
    if request.method == "POST":
        return render(request,'accountapp/hello_world.html', context={'text' : 'POST METHOD!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!'})

