from django.http import HttpResponse
from django.shortcuts import render
import re
from django.utils.timezone import datetime

# Create your views here.
# def home(request):
#     return HttpResponse("Hello, Django!")

def home(request):
    return HttpResponse("Hello to new project")

def hello_there(request, name):
    return render(
        request,
        'projectcsv/index.html',
        {
            'name': name,
            'date': datetime.now()
        }

    )
    
   