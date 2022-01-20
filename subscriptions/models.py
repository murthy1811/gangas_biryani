from django.db import models

# Code has been taken from 'https://github.com/ErnestaMajute/lucentCavern/blob/master/subscriptions/views.py'.
# This code has been taken to save some time and also to learn the method and implement in my own reviews app

class SubscriptionUser(models.Model):
    email = models.EmailField(default=False, null=False, blank=False)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
        