from django.db import models
from django.contrib.auth.models import User
from dishes.models import Dish

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    select_dish = models.ForeignKey( Dish, on_delete=models.CASCADE, null=False, blank=False, default=0)
    message = models.CharField(max_length=600, null=False, blank=False, default=0)









