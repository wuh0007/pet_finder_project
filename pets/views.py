from django.shortcuts import render, get_object_or_404
from .models import Pet
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def pets(request):
    pets = Pet.objects.order_by('-created_date')
    paginator = Paginator(pets, 4)
    page = request.GET.get('page')
    paged_pets = paginator.get_page(page)
    pet_title_search = Pet.objects.values_list('pet_title', flat=True).distinct()
    pet_type_search = Pet.objects.values_list('pet_type', flat=True).distinct()
    pet_breed_search = Pet.objects.values_list('pet_breed', flat=True).distinct()
    age_search = Pet.objects.values_list('age', flat=True).distinct()
    state_search = Pet.objects.values_list('state', flat=True).distinct()
    color_search = Pet.objects.values_list('color', flat=True).distinct()
    gender_search = Pet.objects.values_list('gender', flat=True).distinct()

    data = {
        'pets' : paged_pets,
        'pet_title_search': pet_title_search,
        'pet_type_search': pet_type_search,
        'pet_breed_search': pet_breed_search,
        'age_search': age_search,
        'state_search': state_search,
        'color_search': color_search,
        'gender_search': gender_search,
    }
    return render(request, 'pets/pets.html', data)

def pet_detail(request, id):
    single_pet = get_object_or_404(Pet, pk=id)
    print(single_pet)
    data = {
        'single_pet' : single_pet,
    }
    return render(request, 'pets/pet_detail.html', data)

def search(request):
    pets = Pet.objects.order_by('-created_date')

    pet_title_search = Pet.objects.values_list('pet_title', flat=True).distinct()
    pet_type_search = Pet.objects.values_list('pet_type', flat=True).distinct()
    pet_breed_search = Pet.objects.values_list('pet_breed', flat=True).distinct()
    age_search = Pet.objects.values_list('age', flat=True).distinct()
    state_search = Pet.objects.values_list('state', flat=True).distinct()
    color_search = Pet.objects.values_list('color', flat=True).distinct()
    gender_search = Pet.objects.values_list('gender', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            pets = pets.filter(description__icontains=keyword)

    if 'pet_type' in request.GET:
        keyword = request.GET['pet_type']
        if keyword:
            pets = pets.filter(pet_type__iexact=keyword)

    if 'age' in request.GET:
        keyword = request.GET['age']
        if keyword:
            pets = pets.filter(age__iexact=keyword)

    if 'state' in request.GET:
        keyword = request.GET['state']
        if keyword:
            pets = pets.filter(state__iexact=keyword)

    if 'color' in request.GET:
        keyword = request.GET['color']
        if keyword:
            pets = pets.filter(color__iexact=keyword)

    if 'gender' in request.GET:
        keyword = request.GET['gender']
        if keyword:
            pets = pets.filter(gender__iexact=keyword)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            pets = pets.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'pets' : pets,
        'pet_title_search': pet_title_search,
        'pet_type_search': pet_type_search,
        'pet_breed_search': pet_breed_search,
        'age_search': age_search,
        'state_search': state_search,
        'color_search': color_search,
        'gender_search': gender_search,
    }

    return render(request, 'pets/search.html', data)
