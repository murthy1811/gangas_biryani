from django.db import models
from dishes.models import Dish


class ReviewDish(models.Model):
    message = models.CharField(max_length=600, null=False, blank=False, default=False)
    dish = models.CharField(max_length=400, null=False, blank=False, default=False)
    star = models.CharField(max_length=800, null=False, blank=False, default=False)
    
    def __str__(self):
        return self.message
