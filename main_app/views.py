from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #res.send in express
from .models import Sneaker #importing our model



def home(request):
	return HttpResponse('<h1>Welcome to Sneaker Collector!</>')

def about(request):
	return render(request, 'about.html')

def sneakers_index(request):
	sneakers = Sneaker.objects.all() # using our model to get all the rows in our cat table in psql
	return render(request, 'sneakers/index.html', {'sneakers': sneakers})

def sneakers_detail(request, sneaker_id): # path('cats/<int:cat_id>/' <- this is where cat_id comes from
	sneaker = Sneaker.objects.get(id=sneaker_id)
	return render(request, 'sneakers/detail.html', {'sneaker': sneaker})

