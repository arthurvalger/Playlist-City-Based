from django.db import models

# Create your models here.

class Playlist(models.Model):
    cidade = models.CharField(max_length=30)
    temp = models.CharField(max_length=10, blank=True)
    playlist = models.CharField(max_length=30, blank=True)
    musica = models.CharField(max_length=40, blank=True)
    def __str__(self):
        return self.cidade