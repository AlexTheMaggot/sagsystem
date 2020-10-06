from django.urls import path
from . import views

urlpatterns = [
    path('', views.tenders, name='tenders'),
    path('new/', views.new_tender, name='new_tender'),
    path('new/add', views.tender_add, name='add_tender'),
    path('<int:id>/', views.tender_detail),
    path('<int:id>/delete/', views.tender_delete),
    path('products/', views.product_list),
    path('products/add', views.product_add),
    path('products/<int:id>/delete/', views.product_delete),
    path('products/<int:id>/edit/', views.product_edit),
    path('providers/', views.provider_list),
]
