from django.urls import path

from reviews import views


urlpatterns = [
    path('reviews/',
         views.all_reviews,
         name='reviews'),
]
