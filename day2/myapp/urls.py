from django.urls import path
from myapp import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.registerform,name=""),
]


