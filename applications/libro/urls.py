from django.contrib import admin
from django.urls import path
from .views import ListLibros
from . import views

urlpatterns = [
    path(
        "libros/",
        ListLibros.as_view() 
        ,
        name="libros"
        ),
]