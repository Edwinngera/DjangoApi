from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home, name='index'),
    path('v1/', views.api_test, name='test')]
    
