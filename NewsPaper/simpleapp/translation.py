from .models import Category, Product
from modeltranslation.translator import register, TranslationOptions # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться
 
 
# регистрируем наши модели для перевода
 
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', ) # указываем, какие именно поля надо переводить в виде кортежа
 
 
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', )