from django.shortcuts import render
from .models import Film

# Create your views here.


def home(request):
	film_obj = Film.objects.all()
	data = {"films": film_obj}

	return render(request, "db_homework/home.html", data)