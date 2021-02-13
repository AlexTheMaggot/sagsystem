# InternalImports
from . import views
# End InternalImports

# DjangoImports
from django.urls import path
# End DjangoImports


app_name = 'customers'

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('add/', views.customer_add, name='customer_add'),
    path('<int:customer_id>/edit/', views.customer_edit, name='customer_edit'),
    path('<int:customer_id>/delete/', views.customer_delete, name='customer_delete'),
    path('delete-bulk/', views.customer_delete_bulk, name='customer_delete_bulk'),
    path('add-by_xlsx/', views.customer_add_by_xlsx, name='customer_add_by_xlsx'),
    path('export/', views.customer_export, name='customer_export'),
    path('export/ready/', views.customer_export_ready, name='customer_export_ready')
]