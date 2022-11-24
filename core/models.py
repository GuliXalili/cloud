from django.db import models

class Party(models.Model):
    title = models.CharField(max_length=255)
    atributs = models.TextField()
    dateof = models.CharField(max_length=90)
    location = models.TextField()
    img = models.TextField()

    def __str__(self):
        return self.title
