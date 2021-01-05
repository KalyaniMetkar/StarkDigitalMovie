from django.contrib import admin
from movieratingapp.models import Genre, Movie, Images
# Register your models here.


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Images)
