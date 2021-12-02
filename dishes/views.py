from django.shortcuts import render
from .models import Dish

# Create your views here.

def all_dishes(request):
    """ A view to show all dishes, including sorting and search queries """

    dishes = Dish.objects.all()

    context = {
        'dishes': dishes,
    }

    return render(request, 'dishes/dishes.html', context)