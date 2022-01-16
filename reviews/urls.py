# from django.urls import path
# # from reviews.views import RatingView
# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     path('', views.all_reviews, name='reviews'),
# ]


from django.urls import path

from reviews import views


urlpatterns = [
    path('reviews/',
         views.all_reviews,
         name='reviews'),
]
