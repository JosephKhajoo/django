from django.db import models

# Create your models here.

class Film(models.Model):
	name = models.CharField(max_length=60)
	description = models.TextField()
	release_date = models.IntegerField()
	rating = models.FloatField()

	def __str__(self):
		return self.name