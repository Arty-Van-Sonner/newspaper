from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.utils.translation import gettext as _ # импортируем функцию для перевода
# Create your views here.
 
class Index(View):
    def get(self, request):
        string = _('Hello world') 
   
        return HttpResponse(string)