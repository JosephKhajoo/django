from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

dict_ = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


def greeting(request):
	context = {'name': "Suleyman", 'surname': "Brnakal", 'numbers': [i for i in range(4)]}
	return render(request, "first_app/home.html", context)


def intro(request):
	return HttpResponse("<h1>Introduction</h1><br><p>This is my first website made with django!</p>")


def home(request):
	return redirect("greeting_page")


def dictionary(request):
	final = []
	for key, val in dict_.items():
		final.append(f"{key} : {val},<br>")
	return HttpResponse(final)


def date(request):
    current = datetime.now()
    return HttpResponse(f"<h1>{current}</h1>")