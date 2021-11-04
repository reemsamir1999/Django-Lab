from django.urls import path
from .views import *


urlpatterns = [
    path('', tasks ,name='tasks'),
    path('detail/<int:pk>', detail ,name='detail'),
    path('update/<int:pk>', update ,name='update'),
    path('delete/<int:pk>', delete ,name='delete'),
]