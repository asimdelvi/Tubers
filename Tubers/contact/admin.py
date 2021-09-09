from django.contrib import admin
from .models import Hiretuber, ContactAdmin
# Register your models here.

class HiretuberAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'tuber_name',)

  @admin.display(description="Name")
  def full_name(self, obj):
    return obj.first_name + ' ' + obj.last_name

class ContactAdmin_Admin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'company_name', 'subject')

admin.site.register(Hiretuber, HiretuberAdmin)
admin.site.register(ContactAdmin, ContactAdmin_Admin)