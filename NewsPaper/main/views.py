from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse #  импортируем респонс для проверки текста
 
from django.utils.translation import gettext as _ #  импортируем функцию для перевода
#from django.utils.translation import activate, get_supported_language_variant, LANGUAGE_SESSION_KEY
 
from simpleapp.models import Category
 
from django.utils import timezone
from django.shortcuts import redirect
 
 
import pytz #  импортируем стандартный модуль для работы с часовыми поясами
 
 
class Index(View):
    def get(self, request):

        models = Category.objects.all()
 
        context = {
            'models': models,
            'current_time': timezone.localtime(timezone.now()),
            'timezones': pytz.common_timezones #  добавляем в контекст все доступные часовые пояса
        }
        
        return HttpResponse(render(request, 'index.html', context))
 
    #  по пост-запросу будем добавлять в сессию часовой пояс, который и будет обрабатываться написанным нами ранее middleware
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')