from django.shortcuts import render
import requests
import urllib.request
from rest_framework.response import Response
# Create your views here.
# PRESENT_URL = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=b10b0d059ae2804b6fe8d904c581e3f9&targetDt=20221114"
# listdata = requests.get(PRESENT_URL)
# resDatas = listdata.json().get('boxOfficeResult')

# print(resDatas.get('dailyBoxOfficeList')[0].get('movieNm'))
temp_list=[]
movie_list=[]
def presentmovie(request):
    PRESENT_URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=20221114"
    listdata = requests.get(PRESENT_URL)
    resDatas = listdata.json().get('boxOfficeResult')
    for i in range(10):
        # resDatas.get('dailyBoxOfficeList')[i].get('movieNm')
        temp=resDatas.get('dailyBoxOfficeList')[i].get('movieNm')
        # if temp == '공조2: 인터내셔날':
        #     movie_list.append('공조 2: 인터내셔날')
        # else:
        temp_list.append(temp)
    # for j in movie_list:
    #     EN_URL = f'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={j}'
    #     enlistdata = requests.get(EN_URL)
    #     enresdatas = enlistdata.json().get('movieListResult')
    #     enmovie_list.append(enresdatas.get('movieList')[0].get('movieNmEn'))
    for j in temp_list:
        TMDB_URL=f"https://api.themoviedb.org/3/search/movie?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR&query={j}&page=1&include_adult=false"
        tmdblistdata = requests.get(TMDB_URL)
        tmdbresdatas = tmdblistdata.json().get('results')
        movie_list.append(tmdbresdatas[0].get('title'))
    print(movie_list)
    return Response(resDatas)