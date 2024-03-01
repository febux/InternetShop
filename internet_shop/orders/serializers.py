from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'date_created',
            'paid',
        ]
