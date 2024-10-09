from django.shortcuts import render
from django.http import HttpResponse
from myapp.form import customform

from myapp.form import register


# Create your views here.
def login(req):
    form = customform()
    return render(req,'login.html',{'custform':form})


def registerform(request):
    form = register()
    return render(request, 'register.html', {'regform': form})

