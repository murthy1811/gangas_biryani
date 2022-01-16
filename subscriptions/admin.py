from django.contrib import admin

# Register your models here.
from.models import SubscriptionUser


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscription_date',)


admin.site.register(SubscriptionUser, SubscriptionsAdmin)
