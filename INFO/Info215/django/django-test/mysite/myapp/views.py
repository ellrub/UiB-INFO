from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):

    quotes = ['The greatest glory', 
              'The way to get started is to quit', 
              'If life were predictable it would', 
              'If you set your goals']
    
    quote = random.choice(quotes)
    context = {'quote': quote}

    return render(request, 'index.html', context)