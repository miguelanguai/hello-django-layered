from django.urls import path
from .views import ProductView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product_get'),  # Lista y creación de productos
    path('products/<int:product_id>/', ProductView.as_view(), name='product_rest'),  # Recuperar, actualizar y eliminar un producto
]
