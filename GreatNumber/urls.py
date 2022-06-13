


from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('high/',views.high),
    path('low/',views.low),
    path('right/',views.right),


]

