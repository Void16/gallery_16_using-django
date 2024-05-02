from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'Photo {self.pk}'

class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.pk} on Photo {self.photo.pk}'

class Rating(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE,related_name='ratings')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Rating {self.pk} on Photo {self.photo.pk}'