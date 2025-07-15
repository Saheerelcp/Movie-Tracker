from django.urls import path
from movieapp.views import login,register,registerpost,loginpost,home,search_movie,movie_add,movieList,updatestatus,deletemovie,statusfilter

urlpatterns= [
    path('',login),
    path('register',register),
    path('registerpost',registerpost),
    path('loginpost',loginpost),
    path('home',home),
    path('search/',search_movie,name='search_movie'),
    path('movie_add/<id>',movie_add),
    path('movielist',movieList),
    path('updatestatus/<id>',updatestatus),
    path('deletemovie/<id>',deletemovie),
    path('statusfilter/<str:status>/',statusfilter)
]