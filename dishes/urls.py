from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_dishes, name='dishes'),
    path('<dish_id>', views.dish_detail, name='dish_detail'),
]
