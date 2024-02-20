from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductList, ProductDetails, HomeView

urlpatterns = [
    path("", cache_page(60 * 2)(HomeView.as_view()), name="home"),
    path("products/", cache_page(60 * 5)(ProductList.as_view()), name="products"),
    path("products/<int:pk>/", cache_page(60 * 15)(ProductDetails.as_view()), name="product_details"),
]
