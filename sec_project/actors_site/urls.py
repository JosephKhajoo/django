from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting, name="greeting_page"),
    path('actors', views.actors, name="actors_page"),
]