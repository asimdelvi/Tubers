from .models import Slider, Team, About
from django.shortcuts import render
from youtubers.models import Youtuber

# Create your views here.
def home(request):
  sliders = Slider.objects.all()
  teams = Team.objects.all()
  featured_youtubers = Youtuber.objects.filter(is_featured= True).order_by('-created_date')
  all_youtubers = Youtuber.objects.order_by('is_featured', '-created_date')[0:6]
  data = {
    'sliders': sliders,
    'teams': teams,
    'featured_youtubers': featured_youtubers,
    'all_youtubers': all_youtubers,
  }
  return render(request, 'webpages/home.html', data)


def about(request):
  team = Team.objects.all()
  about_list = About.objects.all()

  data = {
    'team': team,
    'about_list': about_list,
  }

  return render(request, 'webpages/about.html', data)

def services(request):
  return render(request, 'webpages/services.html')
