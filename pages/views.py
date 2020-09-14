from django.shortcuts import render
from .models import Team
from pets.models import Pet

def home(request):
    teams = Team.objects.all()
    featured_pets = Pet.objects.order_by('-created_date').filter(is_featured=True)
    all_pets = Pet.objects.order_by('-created_date')
    data = {
        'teams' : teams,
        'featured_pets' : featured_pets,
        'all_pets' : all_pets,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
