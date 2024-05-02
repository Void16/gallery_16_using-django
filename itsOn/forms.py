from django import forms
from .models import Photo, Comment, Rating

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image',)

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

class RatingForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5)