from django.contrib import admin

# Register your models here.

from bakeryapp.models import Bakery
@admin.register(Bakery)

class BakeryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','text','weight', 'image']
    search_fields = ['name', 'text', 'weight']

