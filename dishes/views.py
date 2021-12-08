from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Dish, Category

# Create your views here.

def all_dishes(request):
    """ A view to show all dishes, including sorting and search queries """

    dishes = Dish.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                dishes = dishes.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            dishes = dishes.order_by(sortkey)

   
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            dishes = dishes.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('dishes'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            dishes = dishes.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'dishes': dishes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'dishes/dishes.html', context)

def dish_detail(request, dish_id):
    """ A view to show individual dish details """

    dish = get_object_or_404(Dish, pk=dish_id)

    context = {
        'dish': dish,
    }

    return render(request, 'dishes/dish_detail.html', context)
