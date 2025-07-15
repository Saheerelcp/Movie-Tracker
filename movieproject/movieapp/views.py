from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from movieapp.models import movies, user
import requests
# Create your views here.
def login(request):
    return render(request,"login.html")
def loginpost(request):
    username = request.POST['username']
    password = request.POST['password']
    
    try:
        us = user.objects.get(username=username)
        print('what is us',us)
        if username == us.username :
            print(password,'password')
            print('database passoword',us.password)
            if password ==us.password :
                request.session['user_id'] = us.id
                return redirect('/home')
            else:
                return render(request,'login.html',{'message':'Incorrect password'})
    except Exception as e:
        print('error',e)
        return render(request,'login.html',{'message':'No user exist'})

def register(request):
    return render(request,'register.html')
def registerpost(request):
    username = request.POST['username']
    password = request.POST['password1']
    obj = user()
    obj.username = username
    obj.password = password
    obj.save()
    return redirect('/')
def home(request):
    userid=request.session.get('user_id')
    us = user.objects.get(id=userid)
    return render(request,'home.html',{'data':us})

def search_movie(request):
    query = request.GET.get('query')
    if not query:
        return JsonResponse({'results': []})

    api_key = 'c61b2f1'  #http://www.omdbapi.com/?i=tt3896198&apikey=c61b2f1
    url =  f'http://www.omdbapi.com/?apikey={api_key}&s={query}'
    response = requests.get(url)
    return JsonResponse(response.json())

def movieList(request):
    userid = request.session.get('user_id')
    mlist = user.objects.get(id=userid)
    usermovies = movies.objects.filter(userid=mlist)
    return render(request,'movielist.html',{'data':usermovies})
def movie_add(request,id):
    # userid= request.session.get('user_id')
    
    movieintance = movies.objects.filter(userid=id).values()
    usr = user.objects.get(id=id)
    poster = request.POST['poster']
    title = request.POST['title']
    year = request.POST['year']
    status = "willwatch"
    for i in movieintance:
        
            
        if i['title'] == title:
            print(i)
            print(title)
            return render(request,'home.html',{'message':'Already added'})
       
    obj = movies()
    obj.userid = usr
    obj.poster = poster
    obj.title = title
    obj.year = year
    obj.status = status
    obj.save()
                
    return redirect('/movielist')

def updatestatus(request,id):
   
    userid = request.session.get('user_id')
    status = request.POST['status']
    movies.objects.filter(id=id,userid=userid).update(status=status)
    
    return redirect('/movielist')

def deletemovie(request,id):
    userid = request.session.get('user_id')
    movies.objects.get(id=id,userid=userid).delete()
    return redirect('/movielist')
def statusfilter(request,status):
    
    userid=request.session.get('user_id')
    filtermovie=movies.objects.filter(status=status,userid=userid)
    if len(filtermovie) > 0:
        print('filtermovie',filtermovie)
        return render(request,'movielist.html',{'data':filtermovie})
    else:
        return render(request,'movielist.html',{'message':f'No movie in {status} list'})
