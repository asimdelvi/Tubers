from .models import Information

def admin_info(request):
  info = Information.objects.filter(on_display=True)[0]
  return {
    'info': info,
  }
