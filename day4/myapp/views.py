from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(req):
    return render(req,'myapp/myappindex.html')



def userid(req,id):

    d=[]
    for i in range(1,11):
        td=str(id)+'X'+str(i)+"="+str(id*i)
        d.append(td)

    return render(req,'myapp/useriddisplay.html',{'tables':d})



def username(req,name):
    return HttpResponse(name)


