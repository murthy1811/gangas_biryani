from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin) :
    readonly_fields = ('user','select_dish', 'message')
    fields = ('user', 'select_dish', 'message')

admin.site.register(Review, ReviewAdmin)
