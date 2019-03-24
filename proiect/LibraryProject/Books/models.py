from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    description = models.TextField()
    releaseDate = models.DateField()
    author = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    image = models.ImageField(blank = True)
    inStock = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def getShortDescription(self):
        return self.description[:50] + "..."