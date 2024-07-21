from django.urls import path, include, re_path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
    path('register/', views.register, name='register'),
    path('login/', views.authenticate_user, name='login'),
    path('user/', views.show_user, name='show_user'),
name='authenticate_user')

]

