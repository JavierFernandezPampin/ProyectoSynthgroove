from django.db import models

# ARTISTS
class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name


# RELEASES
class Release(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    image = models.URLField()
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='releases')

    def __str__(self):
        return self.title


# PODCASTS
class Podcast(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    image = models.URLField()
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='podcasts')

    def __str__(self):
        return self.title


# EVENTS
class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    image = models.URLField()

    def __str__(self):
        return self.name


# CATEGORIES
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# PRODUCTS
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


# NEWSLETTER
class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email