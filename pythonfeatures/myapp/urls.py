from django.urls import path

from . import views


urlpatterns = [
    path("", views.home,name="home"),
    path("weatherinfo/", views.weatherinfo, name="weatherinfo"),
    path("contactmail/",views.contactmail , name = "contactmail"),
    path("Login/",views.login,name="login"),
    path("SignUp",views.Signup,name="SignUp"),
    path("bhargav",views.bhargav,name="bhargav"),

]