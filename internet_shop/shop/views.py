from django.views.generic import ListView, DetailView, TemplateView

from .models import Product


class ProductList(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = "Products"
        return context


class ProductDetails(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = "Product"
        return context


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = "Home"
        return context
