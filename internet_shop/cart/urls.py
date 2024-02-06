from django.urls import path

from .views import cart_details, cart_remove, cart_add

urlpatterns = [
    path('', cart_details, name='cart_details'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
]
