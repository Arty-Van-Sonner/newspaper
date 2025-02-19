from django.contrib import admin
from .models import *
 
# создаём новый класс для представления товаров в админке
# class ProductAdmin(admin.ModelAdmin):
#     # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
#     list_display = tuple(('name', 'price',)) # генерируем список имён всех полей для более красивого отображения
 
 # создаём новый класс для представления товаров в админке
class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('name', 'price', 'on_stock') # оставляем только имя и цену товара
    list_filter = ('price', 'quantity', 'name') # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category__name') # тут всё очень похоже на фильтры из запросов в базу
 
# Register your models here.
admin.site.register(Product, ProductAdmin)

# Register your models here.

admin.site.register(Category)
admin.site.register(Material)
admin.site.register(ProductMaterial)
