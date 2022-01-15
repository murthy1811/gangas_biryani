from django.contrib import admin
from .models import Review

class RatingAdmin(admin.ModelAdmin):
    fields = ('post',)
    list_display = ('post',)
    
admin.site.register(Review)
