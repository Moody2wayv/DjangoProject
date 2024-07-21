from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Landing page
    path('about/', views.about, name='about'),    # About page
    path('shopping/', views.shopping, name='shopping'), # Shopping page
]
