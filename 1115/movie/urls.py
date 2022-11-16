from django.urls import path
from . import views

urlpatterns = [
    path('call/',views.callmovie),
    path('movielist/',views.movie_list),    
    path('movie_detail/<int:movie_pk>/',views.movie_detail)
    
]
