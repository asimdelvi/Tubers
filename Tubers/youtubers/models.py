from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Youtuber(models.Model):

  crew_choices = (
    ('solo', 'solo'),
    ('small', 'small'),
    ('large', 'large'),
  )

  camera_choice = (
    ('canon', 'canon'),
    ('nikon', 'nikon'),
    ('sony', 'sony'),
    ('red', 'red'),
    ('fuji', 'fuji'),
    ('panasonic', 'panasonic'),
    ('others', 'others'),
  )

  category_choice = (
    ('code', 'code'),
    ('tech_review', 'tech_review'),
    ('vlogs', 'vlogs'),
    ('comedy', 'comedy'),
    ('education', 'education'),
    ('science', 'science'),
    ('others', 'others'),
  )

  name = models.CharField(max_length=100)
  price = models.IntegerField()
  photo = models.ImageField(upload_to='media/ytubers/%Y/%m')
  video_url = models.CharField(max_length=255)
  description = RichTextField()
  city = models.CharField(max_length=100)
  age = models.IntegerField()
  height = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null= True)
  crew = models.CharField(choices = crew_choices,max_length=100)
  camera_type = models.CharField(choices= camera_choice, max_length=100)
  subs_count = models.CharField(max_length=100)
  category = models.CharField(choices=category_choice, max_length=100)
  is_featured = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=datetime.now, blank=True)
