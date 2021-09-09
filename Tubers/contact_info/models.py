from django.db import models

# Create your models here.
class Information(models.Model):
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length=20)
  facebook = models.URLField(max_length=200)
  instagram = models.URLField(max_length=200)
  twitter = models.URLField(max_length=200)
  youtube = models.URLField(max_length=200)
  on_display = models.BooleanField()

