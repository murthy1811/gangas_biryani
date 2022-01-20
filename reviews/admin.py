from django.contrib import admin

# Register your models here.
from.models import ReviewDish


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('message',)


admin.site.register(ReviewDish, ReviewsAdmin)
