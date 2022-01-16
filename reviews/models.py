# from django.db import models
# from django.contrib.auth.models import User
# from dishes.models import Dish


# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,)
#     select_dish = models.ForeignKey( Dish, on_delete=models.CASCADE, null=False, blank=False, default='1')
#     message = models.CharField(max_length=600, null=False, blank=False, default='Your thoughts')


from django.db import models


class ReviewDish(models.Model):
    message = models.CharField(max_length=600, null=False, blank=False, default=False)

    def __str__(self):
        return self.message
            

   









