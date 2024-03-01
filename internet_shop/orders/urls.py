from django.urls import path

from .views import order_create, OrderDetail

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('api/order/<int:pk>/', OrderDetail.as_view(), name='api_order_details'),
]
