from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    text = models.TextField()
    image = models.ImageField(upload_to='blog_media/')