from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:placename>/', views.place, name='place'),
    path('restaurant_type/<str:typename>/', views.rst_type, name='rst_type'),
    path('restaurant/<str:restname>', views.restaurant, name='restaurant')
    ]