from django.contrib import messages
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Hiretuber(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=100,blank=True)
  message = models.TextField(blank=True)
  user_id = models.IntegerField(blank=True)
  tuber_id = models.IntegerField()
  tuber_name = models.CharField(max_length=100)
  created_date = models.DateTimeField(blank=True,default= datetime.now)

  def __str__(self):
      return self.email

class ContactAdmin(models.Model):
  full_name = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  company_name = models.CharField(max_length=200, blank=True, null=True)
  subject = models.CharField(max_length=100)
  message = models.TextField()
  created_date = models.DateTimeField(blank=True, default=datetime.now)

  def __str__(self):
      return self.full_name


