from rest_framework import serializers
from .models import Recipe, Product
from django.contrib.auth .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username'
            ]
        

class RecipeSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Recipe
        fields= '__all__'
        
        
class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        # fields= [
        #     "title", "description"
        # ]   
        fields= [
            'title',
            'description',
            'time_required',
            'difficulty',
            'rating',
            'user',
            'updated_by'

           
        ]
        
                     
class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields=[
            'title',
            'description',
            'time_required',
            'difficulty',
            'rating'
        ]                      
                     
         
   
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'   