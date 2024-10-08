from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req,'userpanel.html')

def about(req):
    return HttpResponse("This is About")


def basic(req):
    return HttpResponse("this is basic url")


