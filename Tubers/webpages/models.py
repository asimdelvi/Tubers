from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Slider(models.Model):
  headline = models.CharField(max_length=100)
  subtitle = models.CharField(max_length=255)
  button_text = models.CharField(max_length=50)
  photo = models.ImageField(upload_to='media/slides/%Y/%m')
  url = models.URLField(max_length=500)
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.headline

class Team(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  role = models.CharField(max_length=100)
  fb_link = models.URLField(max_length=255)
  insta_link = models.URLField(max_length=255)
  youtube_link = models.URLField(max_length=255)
  photo = models.ImageField(upload_to= 'media/team/%Y/%m/%d/')
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.first_name

class About(models.Model):
  heading = models.CharField(max_length=50)
  about_content = RichTextField()

  def __str__(self):
      return self.heading
