from django.shortcuts import render, get_object_or_404
from .models import Pet
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def pets(request):
    pets = Pet.objects.order_by('-created_date')
    paginator = Paginator(pets, 4)
    page = request.GET.get('page')
    paged_pets = paginator.get_page(page)
    data = {
        'pets' : paged_pets,
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

    # if 'keyword' in request.GET:
    #     keyword = request.GET['keyword']
    #     if keyword:
    #         cars = cars.filter(description__icontains=keyword)

    data = {
        'pets' : pets,
    }

    return render(request, 'pets/search.html', data)
