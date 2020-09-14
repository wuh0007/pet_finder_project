from django.shortcuts import render

def pets(request):
    return render(request, 'pets/pets.html')
