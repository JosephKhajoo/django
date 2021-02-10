from django.contrib import admin
from actors_site.models import *

# Register your models here.

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Genre)