from django.contrib import admin
from .models import Information

# Register your models here.
class InformationAdmin(admin.ModelAdmin):
  list_display = ('id','email', 'phone', 'on_display')
  list_display_links = ('id', 'email')
  list_editable = ('on_display',)


admin.site.register(Information, InformationAdmin)