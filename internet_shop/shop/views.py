from django.views.generic import ListView, DetailView

from .models import Product


class ProductList(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = 'products'
    paginate_by = 3


class ProductDetails(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = 'product'
