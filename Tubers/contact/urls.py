from django.urls import path
from . import views

urlpatterns = [
    path('hiretuber', views.hiretuber, name='hiretuber'),
    path('contact_us', views.contact_admin, name='contact')
]
