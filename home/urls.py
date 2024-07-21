from django.contrib import admin
from home.views import PersonAPI, PeopleViewSet, LoginAPI, RegisterAPI
from django.urls import path, include

urlpatterns = [
    path('details/', PersonAPI.as_view()),
    path('register/login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
]