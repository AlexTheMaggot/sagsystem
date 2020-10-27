from django.urls import path
from . import views


urlpatterns = [
    path('', views.tender_list),
    path('<int:tender_id>/', views.tender_detail),
    path('add/', views.tender_add),
    path('<int:tender_id>/delete/', views.tender_delete),
    path('<int:tender_id>/edit/', views.tender_edit),
    path('<int:tender_id>/participant_add/', views.participant_add),
    path('<int:tender_id>/participants/<int:participant_id>/delete/', views.participant_delete),
    path('<int:tender_id>/goods_add/', views.goods_add),
    path('<int:tender_id>/goods/<int:goods_id>/delete/', views.goods_delete),
    path('<int:tender_id>/prices_edit/', views.prices_edit),
    path('<int:tender_id>/select-winners/', views.select_winners),
    path('<int:tender_id>/delete_selected/', views.select_winners_delete),
    path('products/', views.product_list),
    path('products/category/<int:id>/', views.product_by_category),
    path('products/add/', views.product_add),
    path('products/<int:id>/delete/', views.product_delete),
    path('products/<int:id>/edit/', views.product_edit),
    path('product-category/', views.product_category_list),
    path('product-category/add/', views.product_category_add),
    path('product-category/<int:id>/delete/', views.product_category_delete),
    path('product-category/<int:id>/edit/', views.product_category_edit),
    path('providers/', views.provider_list),
    path('providers/<int:id>/', views.provider_detail),
    path('providers/add/', views.provider_add),
    path('providers/<int:id>/delete/', views.provider_delete),
    path('providers/<int:id>/edit/', views.provider_edit),
]


