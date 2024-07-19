from django.contrib import admin
from home.views import PersonAPI, PeopleViewSet, LoginAPI, RegisterAPI
from django.urls import path, include

urlpatterns = [
    path('persons/', PersonAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
]