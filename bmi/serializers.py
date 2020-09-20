from rest_framework import serializers

from decimal import *

class BMISerializer(serializers.Serializer):

    """Serializers Height and Weight"""
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    height = serializers.DecimalField(max_digits=5, decimal_places=2)
