from django.urls import path

from .views import ProductList, ProductDetails, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductList.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetails.as_view(), name="product_details"),
]
