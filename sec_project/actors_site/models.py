from django.db import models

# Create your models here.

GENRE_CHOICES = (
	(0, "Action"),
	(1, "Drama"),
	(2, "Fantasy")
)


class Genre(models.Model):
	name = models.IntegerField(choices=GENRE_CHOICES)
	description = models.TextField()

	def __str__(self):
		return f"{GENRE_CHOICES[self.name][1]}"

class Actor(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=30)
	desc = models.TextField()
	age = models.IntegerField()
	married = models.BooleanField()

	def __str__(self):
		return f"{self.name} {self.surname}"


class Movie(models.Model):
	name = models.CharField(max_length=20)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	actors = models.ManyToManyField(Actor)

	def __str__(self):
		return f"{self.name} {self.genre}"