from django.contrib import admin
from .models import Slider, Team, About
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):

  @admin.display(description="Photo")
  def team_photo(self, obj):
    return format_html('<img width="50" src="{}"/>'.format(obj.photo.url))

  @admin.display(description="Name")
  def name(self, obj):
    return obj.first_name + ' ' + obj.last_name

  list_display = ('id', 'team_photo', 'name', 'role', 'created_on')
  list_display_links = ('id', 'name')
  search_fields = ('id', 'first_name', 'last_name', 'role')
  list_filter = ('role',)
  ordering = ('id',)

class SliderAdmin(admin.ModelAdmin):
  @admin.display(description="Photo")
  def slider_photo(self, obj):
    return format_html('<img width="100" src="{}"/>'.format(obj.photo.url))

  list_display = ('headline', 'slider_photo', 'button_text')

class AboutAdmin(admin.ModelAdmin):
  list_display = ('id', 'heading')
  list_display_links = ('id', 'heading')

admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(About, AboutAdmin)
