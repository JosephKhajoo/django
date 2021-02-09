from django.shortcuts import render
import json

# Create your views here.


def greeting(request):
	return render(request, "actors_site/greeting.html")


def actors(request):
	with open("data.json", "r") as file:
		data = json.load(file)

	return render(request, "actors_site/actors.html", data)