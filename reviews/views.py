from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from dishes.models import Dish
from .models import ReviewDish


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














# from django.shortcuts import render, redirect, reverse
# from dishes.models import Dish
# from django.contrib import messages
# from reviews.forms import RatingForm



# def all_reviews(request):
#     dishes = Dish.objects.all()
#     rating_form = RatingForm()
#     template = 'reviews/reviews.html'
#     context = {
#         'rating_form' : rating_form,
#         'dishes': dishes,
#     }
#     if rating_form.is_valid():
#         select_dish = form.cleaned_data['dish_select']
#         message = form.cleaned_data['message']
#         review = rating_form.save(commit=False)
#         review.save()

#     return render(request, template, context)



# def all_reviews(request):
#     dishes = Dish.objects.all()
#     context = {
#         'dishes': dishes,
#     }
#     return render(request, 'reviews/reviews.html', context)

# class RatingView(TemplateView):
#     template_name = 'reviews/reviews.html'




# def post(self, request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = RatingForm(request.POST)
        
#         # check whether it's valid:
#         if form.is_valid():
#             form.save()
#             dish_select = form.cleaned_data['dish_select']
#             message = form.cleaned_data['message']
            
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = RatingForm()
    
#     return render(request, 'reviews/reviews.html', context)

    

# def get(self, request):
#         form = RatingForm()
#         return render(request, 'reviews/reviews.html', {'form': form})

# def post(self,request):
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             comment = form.cleaned_data['post']            
#             form = RatingForm()
#         args = {'form': form, 'comment': comment}
#         return render(request, self.template_name, args)
