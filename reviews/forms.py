from django import forms
from reviews.models import Review

class RatingForm(forms.ModelForm):
    dish_select = forms.CharField(label='dish_select', max_length=100)
    message = forms.CharField(label='textfeedback', max_length=800)
    class Meta:
        model = Review
        fields = ('dish_select', 'message',)

 