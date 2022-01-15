from django.shortcuts import render
from dishes.models import Dish
from django.views.generic import TemplateView
from reviews.forms import RatingForm


def all_reviews(request):
    dishes = Dish.objects.all()
    context = {
        'dishes': dishes,
    }
    return render(request, 'reviews/reviews.html', context)

# class RatingView(TemplateView):
#     template_name = 'reviews/reviews.html'




def post(self, request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RatingForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            form.save()
            dish_select = form.cleaned_data['dish_select']
            message = form.cleaned_data['message']
            
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RatingForm()
    
    return render(request, 'reviews/reviews.html', context)

    

# def get(self, request):
#         form = RatingForm()
#         return render(request, self.template_name, {'form': form})

# def post(self,request):
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             comment = form.cleaned_data['post']            
#             form = RatingForm()
#         args = {'form': form, 'comment': comment}
#         return render(request, self.template_name, args)
