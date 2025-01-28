from django.urls import path
from .views import IndexView, NewOrderView, take_order

urlpatterns = [
    path('', IndexView.as_view()),
    path('new/', NewOrderView.as_view(), name = 'new_order'),
    path('take/<int:oid>', take_order, name = 'take_order')
]