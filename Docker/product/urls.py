from django.urls import path
from .views import ProductDetail, ProductList, ProductCreate

app_name = "product"
urlpatterns = [
    path('list/',ProductList.as_view(), name = "list_products"),
    path('<int:pk>/',ProductDetail.as_view(), name = "product_detail"),  # <int:pk> is a placeholder for the primary key of the Product model.
    path('create/', ProductCreate.as_view(), name = "create_product"),  # Create a new product.  # This URL is for creating a new product. The view will be ProductCreate.as_view().
]