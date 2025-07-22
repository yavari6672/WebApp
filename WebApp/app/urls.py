from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('app_list/', views.app_list, name='app_list'),

]
