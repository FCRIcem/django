
from django.urls import path
from .views import *

urlpatterns = [
    path("quiz/<int:baslik_id>",index,name='index'),
    path("sonuc/<int:baslik_id>",sonuc,name='sonuc'),
]