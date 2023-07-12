from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.movies.clear()  # Remove associations with movies
        super().delete(*args, **kwargs)
    

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=255)
    img_url = models.URLField()
    year = models.PositiveIntegerField()    # only year info instead of full date
    run_time = models.CharField(max_length=20)     # data looks like  runtime	"2h 8m"
    star = models.DecimalField(max_digits=2, decimal_places=1)
    count = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    language = models.CharField(max_length=100)
    description = models.TextField()
    is_watched = models.BooleanField(default=False)
    collections = models.ManyToManyField(Collection, related_name='movies')
    imdb_id=models.CharField(max_length=20,unique=True)  # identifier 

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        print("Entered!")
        self.genres.clear()  # Remove associations with genres
        super().delete(*args, **kwargs)