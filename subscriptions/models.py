from django.db import models


class SubscriptionUser(models.Model):
    email = models.EmailField(default=False, null=False, blank=False)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
        