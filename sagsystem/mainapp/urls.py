from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('workers/', views.workers_list, name='workers_list'),
    path('auth/', views.AuthLoginView.as_view(), name='auth'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('auth/check/', views.auth_check, name='auth_check'),
    path('measures/', views.measures_list),
    path('measures/add', views.measures_add),
    path('measures/<int:id>/delete', views.measures_delete),
    path('measures/<int:id>/edit', views.measures_edit),
    path('access-denied/', views.access_denied, name='access-denied')
]