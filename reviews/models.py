from django.db import models
from django.contrib.auth.models import User
from dishes.models import Dish

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    dish = models.ForeignKey( Dish, on_delete=models.DO_NOTHING, null=False, blank=False, default=0)

    def __str__(self):
        return self.name







