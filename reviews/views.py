from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from dishes.models import Dish
from .models import ReviewDish

# Only code idea has been taken from Subscriptions app (inspired by 'https://github.com/ErnestaMajute/lucentCavern/blob/master/subscriptions/views.py'.
# Several commits have been made to solve this model and finally solved by inspiration, but code is written by me


def all_reviews(request):
    dishes = Dish.objects.all()
    """Allows user to give feedback"""
    redirect_url = request.POST.get('redirect_url')
    context = {
        'dishes' : dishes,
    }

    if request.method == "POST":
        message = request.POST.get('textfeedback')
        dish = request.POST.get('selectdish')
        star = request.POST.get('rating')

        new_message = ReviewDish(message=message, dish=dish, star=star)
        new_message.save()
        messages.success(
            request,
            f'Thanks! Your feedback is much appreciated')

        
    return render(request, 'reviews/reviews.html', context )

