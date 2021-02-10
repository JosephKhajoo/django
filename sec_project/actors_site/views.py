from django.shortcuts import render
from .models import *
import json

# Create your views here.


def greeting(request):
	return render(request, "actors_site/greeting.html")


def actors(request):
	# with open("data.json", "r") as file:
	# 	data = json.load(file)
	actor = Actor.objects.all()
	movie = Movie.objects.all()

	data = {
		"movies": movie,
	}
	
	return render(request, "actors_site/actors.html", data)
