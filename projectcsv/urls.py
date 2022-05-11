from django.urls import path
from projectcsv import views

urlpatterns = [
    path("", views.home, name="home"),
    path("project/<name>",views.hello_there, name="hello_there"),
]