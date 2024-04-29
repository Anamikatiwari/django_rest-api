from rest_framework import serializers
from .models import Recipe, Product

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields= '__all__'
        
   
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'   