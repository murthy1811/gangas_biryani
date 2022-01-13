from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_dishes, name='dishes'),
    path('<int:dish_id>/', views.dish_detail, name='dish_detail'),
    path('add/', views.add_dish, name='add_dish'),
    path('edit/<int:dish_id>/', views.edit_dish, name='edit_dish'),
]
