from django.db import models
from movie.models import Movie
from django.conf import settings
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    movie_title = models.ForeignKey(Movie,on_delete=models.CASCADE)
    content = models.TextField()
    cinema = models.CharField(max_length=100)
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)