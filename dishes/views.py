from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Dish

# Create your views here.

def all_dishes(request):
    """ A view to show all dishes, including sorting and search queries """

    dishes = Dish.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('dishes'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            dishes = dishes.filter(queries)

    context = {
        'dishes': dishes,
        'search_term': query,
    }

    return render(request, 'dishes/dishes.html', context)

def dish_detail(request, dish_id):
    """ A view to show individual dish details """

    dish = get_object_or_404(Dish, pk=dish_id)

    context = {
        'dish': dish,
    }

    return render(request, 'dishes/dish_detail.html', context)
