from django.shortcuts import render
from .models import Team
from pets.models import Pet

def home(request):
    teams = Team.objects.all()
    featured_pets = Pet.objects.order_by('-created_date').filter(is_featured=True)
    all_pets = Pet.objects.order_by('-created_date')
    pet_title_search = Pet.objects.values_list('pet_title', flat=True).distinct()
    pet_type_search = Pet.objects.values_list('pet_type', flat=True).distinct()
    pet_breed_search = Pet.objects.values_list('pet_breed', flat=True).distinct()
    age_search = Pet.objects.values_list('age', flat=True).distinct()
    state_search = Pet.objects.values_list('state', flat=True).distinct()
    color_search = Pet.objects.values_list('color', flat=True).distinct()
    gender_search = Pet.objects.values_list('gender', flat=True).distinct()

    data = {
        'teams' : teams,
        'featured_pets' : featured_pets,
        'all_pets' : all_pets,
        'pet_title_search': pet_title_search,
        'pet_type_search': pet_type_search,
        'pet_breed_search': pet_breed_search,
        'age_search': age_search,
        'state_search': state_search,
        'color_search': color_search,
        'gender_search': gender_search,
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
