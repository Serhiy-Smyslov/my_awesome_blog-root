from django.db import models


# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to='event_images/')
    title = models.CharField(max_length=300)
