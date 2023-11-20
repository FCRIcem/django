from django.urls import path
from .views import *
urlpatterns = [
    path('', giris_yap,name='giris_yap'),
    path('kayit', kayit_ol,name='kayit_ol'),
    path('cikis', cikis,name='cikis'),
]
