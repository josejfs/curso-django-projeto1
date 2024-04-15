from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', context={
        'name': 'José Ferreira',
        })

def contact(request):
    return HttpResponse('<h1>Contact<h1>')

def sobre(request):
    return HttpResponse('<h1>Sobre<h1>')