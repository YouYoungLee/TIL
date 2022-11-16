from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleListSerializer,CommentListSerializer
from .models import Article,Comment
from movie.models import Movie
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def articlecreate(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = ArticleListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_title=movie)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def articleindex(request):
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def articledetail(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # elif request.method == 'PUT':
    #     serializer = ArticleListSerializer(instance=article, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    else: 
        article.delete()
        return Response(data='delete success',status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    serializer = CommentListSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def article_comments(request):
    comments = get_list_or_404(Comment)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

