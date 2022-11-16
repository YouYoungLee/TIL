from rest_framework import serializers
from .models import Article,Comment
from django.contrib.auth import get_user_model
from movie.models import Movie

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('movie_title',)

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
