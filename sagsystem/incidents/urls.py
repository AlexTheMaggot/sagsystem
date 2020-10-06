from django.urls import path

from . import views


urlpatterns = [
    path('', views.incidents_dashboard, name='incidents'),
    path('add/', views.incidents_add, name='incidents_add')
]