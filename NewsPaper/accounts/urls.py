from django.urls import path
from .views import SignUp, logout

urlpatterns = [
    # path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', logout, name='logout')
]