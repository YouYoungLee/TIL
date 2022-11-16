from django.shortcuts import render
import requests
from rest_framework.response import Response
from .models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer
# Create your views here.
# PRESENT_URL = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=b10b0d059ae2804b6fe8d904c581e3f9&targetDt=20221114"
# listdata = requests.get(PRESENT_URL)
# resDatas = listdata.json().get('boxOfficeResult')

# print(resDatas.get('dailyBoxOfficeList')[0].get('movieNm'))
temp_list=[]
movieid_list=[]
movie_list=[]
def callmovie(request):
    PRESENT_URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=20221114"
    listdata = requests.get(PRESENT_URL)
    resDatas = listdata.json().get('boxOfficeResult')
    for i in range(10):
        temp=resDatas.get('dailyBoxOfficeList')[i].get('movieNm')
        temp_list.append(temp)
    for i in temp_list:
        TMDB_URL=f"https://api.themoviedb.org/3/search/movie?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR&query={i}&page=1&include_adult=false"
        tmdblistdata = requests.get(TMDB_URL)
        tmdbresdatas = tmdblistdata.json().get('results')
        movieid_list.append(tmdbresdatas[0].get('id'))
    for i in movieid_list:
        temp_genre=[]
        actor_list=[]
        TMDBDETAIL_URL=f"https://api.themoviedb.org/3/movie/{i}?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR"
        tmdbdetaildata = requests.get(TMDBDETAIL_URL)
        title = tmdbdetaildata.json().get('title')
        release_data = tmdbdetaildata.json().get('release_date')
        vote_average = tmdbdetaildata.json().get('vote_average')
        overview = tmdbdetaildata.json().get('overview')
        for j in range(len(tmdbdetaildata.json().get('genres'))):
            temp_genre.append((tmdbdetaildata.json().get('genres')[j].get('name')))
        genre = temp_genre
        poster_path = tmdbdetaildata.json().get('poster_path')
        runnig_time = tmdbdetaildata.json().get('runtime')
        # print(title,release_data,vote_average,overview,genre,poster_path,runnig_time)
        TMDBCREDITS_URL=f"https://api.themoviedb.org/3/movie/{i}/credits?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR"
        tmdbcreditsdata = requests.get(TMDBCREDITS_URL)
        for k in range(5):
            actor_list.append(tmdbcreditsdata.json().get('cast')[k].get('name'))
        actor = actor_list
        for i in range(20):
            if tmdbcreditsdata.json().get('crew')[i].get('job')=='Director':
                director = tmdbcreditsdata.json().get('crew')[i].get('name')
                break
        movie = Movie(title=title,release_data=release_data,vote_average=vote_average,overview=overview,genre=genre,poster_path=poster_path,actor=actor,director=director,runnig_time=runnig_time)
        movie.save()

        
    return Response(resDatas)

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)

