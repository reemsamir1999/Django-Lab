from django.urls import path
from .views import *


urlpatterns = [
      path('', index ,name='index'),
      path('post/', post ,name='post'),
      path('put/<int:pk>', put ,name='put'),
      path('delete/<int:pk>', delete ,name='delete'),
      path('get/<int:pk>', get ,name='get'),
]