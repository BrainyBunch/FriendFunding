from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()
    def __str__(self):
        return self.name

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goal')
    title=models.CharField(max_length=100, default='no song title')
    album=models.CharField(max_length=100, default='no album title')
    def __str__(self):
        return self.title
