from django.urls import path
from myapp import views

urlpatterns = [
    path('myapp',views.index,name=""),

    path('user/<int:id>',views.userid,name=""),
    path('user/<str:name>',views.username,name="")
]



