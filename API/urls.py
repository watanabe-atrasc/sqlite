from django.urls import path
from . import views

urlpatterns = [
    path('login',views.Login, name='login'),
    path('record',views.Record, name='record'),
    path('getInfo', views.GetInfo, name='getInfo'),
    path('correct', views.Correct, name='correct')
]