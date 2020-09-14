from django.urls import path
from . import views

urlpatterns = [
    path('', views.pets, name='pets'),
    path('<int:id>', views.pet_detail, name='pet_detail'),
    path('search', views.search, name='search')
]
