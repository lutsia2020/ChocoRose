from django.contrib import admin

# Register your models here.

from . models import Bakery, BakeryCategory, BakeryСonsist, BakeryBasis, BakeryCream, BakeryFilling

class BakeryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']


class BakeryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'text','weight', 'price', 'image',]
    search_fields = ['name', 'category__name']

class BakeryConsistAdmin(admin.ModelAdmin):
    list_display = ['customer', 'phone', 'name', 'basis','cream', 'filling','price']
    search_fields = ['customer', 'phone','name', 'basis','cream', 'filling', ]

class BakeryCreamAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',]

class BakeryFillingAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',]

admin.site.register(BakeryCategory, BakeryCategoryAdmin)
admin.site.register(Bakery, BakeryAdmin)
admin.site.register(BakeryСonsist, BakeryConsistAdmin)
admin.site.register(BakeryBasis)
admin.site.register(BakeryCream, BakeryCreamAdmin)
admin.site.register(BakeryFilling, BakeryFillingAdmin)
