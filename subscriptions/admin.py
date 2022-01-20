from django.contrib import admin

# Code has been taken from 'https://github.com/ErnestaMajute/lucentCavern/blob/master/subscriptions/views.py'.
# This code has been taken to save some time and also to learn the method and implement in my own reviews app

# Register your models here.
from.models import SubscriptionUser


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscription_date',)


admin.site.register(SubscriptionUser, SubscriptionsAdmin)
