from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_data = models.DateField()
    vote_average = models.FloatField()
    overview = models.TextField()
    genre = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=200)
    actor = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    runnig_time = models.CharField(max_length=150)
