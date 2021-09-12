from django.shortcuts import get_object_or_404, render
from .models import Youtuber
# Create your views here.

def youtubers(request):
  youtubers = Youtuber.objects.order_by('-created_date')
  city_search = Youtuber.objects.values_list('city', flat=True).distinct()
  camera_type_search = Youtuber.objects.values_list(
      'camera_type', flat=True).distinct()
  category_search = Youtuber.objects.values_list(
      'category', flat=True).distinct()

  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      youtubers = Youtuber.objects.filter(city__iexact=city)

  if 'camera_type' in request.GET:
    camera_type = request.GET['camera_type']
    if camera_type:
      youtubers = Youtuber.objects.filter(camera_type__iexact=camera_type)

  if 'category' in request.GET:
    category = request.GET['category']
    if category:
      youtubers = Youtuber.objects.filter(category__iexact=category)

  data = {
      'youtubers': youtubers,
      'city_list': city_search,
      'camera_type_list': camera_type_search,
      'category_list': category_search,
  }

  return render(request, 'youtubers/youtubers.html', data )

def youtuber_details(request, pk):
  youtuber = get_object_or_404(Youtuber, id= pk)
  # OR
  # youtuber = Youtuber.objects.get(id= pk)
  data = {
    'youtuber': youtuber
  }
  return render(request, 'youtubers/youtuber_details.html', data)

def search(request):
  youtubers = Youtuber.objects.order_by('-created_date')
  city_search = Youtuber.objects.values_list('city', flat=True).distinct()
  camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
  category_search = Youtuber.objects.values_list('category', flat=True).distinct()

  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      youtubers = Youtuber.objects.filter(description__icontains = keyword)

  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      youtubers = Youtuber.objects.filter(city__iexact=city)

  if 'camera_type' in request.GET:
    camera_type = request.GET['camera_type']
    if camera_type :
      youtubers = Youtuber.objects.filter(camera_type__iexact=camera_type)

  if 'category' in request.GET:
    category = request.GET['category']
    if category:
      youtubers = Youtuber.objects.filter(category__iexact=category)

  data = {
    'youtubers': youtubers,
    'city_search': city_search,
    'camera_type_search': camera_type_search,
    'category_search': category_search,
  }

  return render(request, 'youtubers/search.html', data)
