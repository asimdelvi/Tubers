from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.
class YoutubersAdmin(admin.ModelAdmin):
  @admin.display(description="Photo")
  def youtubers_photo(self, obj):
    return format_html('<img width="60" src="{}" />'.format(obj.photo.url))

  list_display = ('id','youtubers_photo','name', 'price', 'subs_count', 'is_featured',)
  list_display_links = ('id', 'youtubers_photo', 'name')
  ordering = ('id',)
  list_filter = ('is_featured',)
  list_editable = ('is_featured', )
  search_fields = ('id', 'name')

admin.site.register(Youtuber, YoutubersAdmin)
