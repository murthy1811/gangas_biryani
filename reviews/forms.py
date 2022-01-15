from django import forms
from reviews.models import Rating

class RatingForm(forms.ModelForm):    
    post = forms.CharField()

    class Meta:
        model = Rating
        fields = ('post',)

 