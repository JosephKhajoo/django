from django.urls import path
from . import views

urlpatterns = [
    path('greeting', views.greeting, name="greeting_page"),
    path('introduction', views.intro, name="intro_page"),
    path('date', views.date, name="date_page"),
    path('dictionary', views.dictionary, name="dictionary_page"),
    path('', views.home, name="home_page"),
]