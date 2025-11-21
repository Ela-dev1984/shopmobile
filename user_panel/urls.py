from django.contrib import admin
from django.urls import path
from .views import all,sort,search


urlpatterns = [
    
    path("all/",all,name="all"),
    path("sort/<int:kamine>/<int:bishine>/",sort,name="sort"),
    path("search/<str:search>/",search, name="search"),
]