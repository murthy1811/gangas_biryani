from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Dish, Category
from .forms import DishForm


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
            
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
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


@login_required
def add_dish(request):
    """ Add a new dish to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save()
            messages.success(
                request, 'Successfully added dish!')
            return redirect(reverse(
                'dish_detail', args=[dish.id]))
        else:
            messages.error(request, 'Failed to add dish.Please ensure the form is valid.')
    else:
        form = DishForm()
    
    template = 'dishes/add_dish.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_dish(request, dish_id):
    """ Edit a dish in the portal """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == 'POST':
        form = DishForm(
            request.POST,
            request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully updated dish!')
            return redirect(reverse(
                'dish_detail', args=[dish.id]))
        else:
            messages.error(request, 'Failed to update dish.Please ensure the form is valid.')
    else:
        form = DishForm(instance=dish)
        messages.info(
            request, f'You are editing {dish.name}')

    template = 'dishes/edit_dish.html'
    context = {
        'form': form,
        'dish': dish,
    }

    return render(request, template, context)
    

@login_required
def delete_dish(request, dish_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    dish = get_object_or_404(Dish, pk=dish_id)
    dish.delete()
    messages.success(request, 'Dish deleted!')
    return redirect(reverse('dishes'))

