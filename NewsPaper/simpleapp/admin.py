from django.contrib import admin
from .models import *
 
# создаём новый класс для представления товаров в админке
class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = tuple(('name', 'price',)) # генерируем список имён всех полей для более красивого отображения
 
 
# Register your models here.
admin.site.register(Product, ProductAdmin)

# Register your models here.

admin.site.register(Category)
admin.site.register(Material)
admin.site.register(ProductMaterial)
