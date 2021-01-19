from django.db import models

# Create your models here.
class History(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url

class Bookmark(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url        