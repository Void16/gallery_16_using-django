from django.shortcuts import render, redirect
from .models import Photo, Comment, Rating
from .forms import PhotoForm, CommentForm, RatingForm

def gallery(request):
    photos = Photo.objects.all()
    top_photos = photos.order_by('-likes')[:5]
    if request.method == 'POST':
        if 'add_photo' in request.POST:
            photo_form = PhotoForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo = photo_form.save()
                return redirect('gallery')
        elif 'add_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                photo_id = request.POST['photo_id']
                comment = comment_form.cleaned_data['comment']
                comment = Comment.objects.create(photo_id=photo_id, comment=comment)
                return redirect('gallery')
        elif 'add_rating' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                photo_id = request.POST['photo_id']
                rating = rating_form.cleaned_data['rating']
                photo = Photo.objects.get(id=photo_id)
                photo.likes += rating
                photo.save()
                return redirect('gallery')
    else:
        photo_form = PhotoForm()
        comment_form = CommentForm()
        rating_form = RatingForm()
    return render(request, 'gallery.html', {'photos': photos, 'top_photos': top_photos, 'photo_form': photo_form, 'comment_form': comment_form, 'rating_form': rating_form})