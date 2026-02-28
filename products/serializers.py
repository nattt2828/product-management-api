from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    # Validation Rule 1
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must not be negative.")
        return value

    # Validation Rule 2
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock must not be below 0.")
        return value
