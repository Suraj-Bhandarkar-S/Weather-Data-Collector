
from django.http import HttpResponse
#from .models import studentform
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from reportlab.pdfgen import canvas
from django.db.models import Count, Q
from django.contrib import auth
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import City,graph
from .forms import CityForm,Inputdata
def index(request):
    return render(request,"GRsystem/Home.html")

def signin(request):
    return render(request,"GRsystem/signin.html")
def login(request):
    return render(request,"GRsystem/login.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
   
        if form.is_valid():
            
            new_user=form.save()
            messages.add_message(request,messages.SUCCESS, f' Registered Successfully ')
            return redirect('/login/')
    else:
        form = UserRegisterForm()
        

    context={'form': form}
    return render(request, 'GRsystem/register.html',context )



@login_required
def dashboard(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        coord=requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'coord':coord,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity':city_weather['main']['humidity'],
          
        }

        weather_data.append(weather) #add the data for the current city into our list
    
    context = {'weather_data' : weather_data, 'form' : form}
        
    return render(request, 'GRsystem/dashboard.html',context)

def stats(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    


    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        wind=requests.get(url.format(city)).json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity':city_weather['main']['humidity'],
            'temp_min':city_weather['main']['temp_min'],
            'temp_max':city_weather['main']['temp_max'],
            'pressure':city_weather['main']['pressure'],
            'wind':city_weather['wind']['speed'],
            'country':city_weather['sys']['country'],
          
        }

        weather_data.append(weather) #add the data for the current city into our list
    
    
    context = {'weather_data' : weather_data, 'form' : form}
        
    return render(request, 'GRsystem/stats.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.add_message(request,messages.SUCCESS, f'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.add_message(request,messages.WARNING, f'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'GRsystem/change_password.html', {
        'form': form
    })

def form(request):
    if request.method=='POST':
        form =Inputdata(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, f'Your Data was successfully added!')
            return redirect('form')
    else:
        form =Inputdata()
    
    context={'form':form}
    return render(request, 'GRsystem/inputform.html',context)


def graphs(request):
    search_query=''
    dataset=''
    datasets=''
    if request.method=='POST':
        search_query = request.POST.get('search')
    
        dataset = graph.objects.values('Temp').filter(city__icontains=search_query).annotate(value=Count('Temp',filter=Q(city__icontains='search_query'))).order_by('Date')
        datasets = graph.objects.values('Date').annotate(value=Count('Temp',filter=Q(city__icontains='search_query'))).order_by('Date')

    args={'dataset':dataset,'datasets':datasets,'search_query':search_query}
    return render(request, 'GRsystem/graph.html',args)

             

