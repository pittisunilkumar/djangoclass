from django.urls import path
from userpanel import views


urlpatterns = [
    path('about',views.about,name="about"),
    path('userpanel',views.index,name="index"),
    path('',views.basic,name="base"),
]
