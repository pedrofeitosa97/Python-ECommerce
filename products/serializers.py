from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    picture_url = serializers.CharField(max_length=255)

    def create(self, validated_data:dict) -> Products:
            return Products.objects.create(**validated_data)
    def update(self, instance: Products, validated_data: dict) -> Products:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()
            return instance