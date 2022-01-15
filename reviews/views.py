from django.shortcuts import render
from dishes.models import Dish


def all_reviews(request):

    dishes = Dish.objects.all()

    context = {
        'dishes': dishes,
    }

    return render(request, 'reviews/reviews.html', context)

   