from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/photodirector')

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/photoactor')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor)
    poster = models.ImageField(upload_to='media/movies')

    def __str__(self):
        return self.title


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    time = models.DateTimeField()
    hall = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.movie.title} - {self.time}'


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.session.movie.title} - {self.seat}"