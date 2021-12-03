from django.shortcuts import render, get_object_or_404
from .models import Dish

# Create your views here.

def all_dishes(request):
    """ A view to show all dishes, including sorting and search queries """

    dishes = Dish.objects.all()

    context = {
        'dishes': dishes,
    }

    return render(request, 'dishes/dishes.html', context)

def dish_detail(request, dish_id):
    """ A view to show individual dish details """

    dish = get_object_or_404(Dish, pk=dish_id)

    context = {
        'dish': dish,
    }

    return render(request, 'dishes/dish_detail.html', context)
