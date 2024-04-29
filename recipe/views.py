from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe, Product
from rest_framework.viewsets import ModelViewSet
from .serializers import RecipeSerializer, ProductSerializer

# Create your views here.


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





@api_view()
def hello(request):
    return Response({
        "data": "Hello, world!"
    })
    
    
    
@api_view(['GET','POST'])
def list_recipe(request):  
    if request.method =="POST":
            print(request.data)
            recipe_serializer= RecipeSerializer(data=request.data)
            if recipe_serializer.is_valid(raise_exception=True):
                recipe_serializer.save()
                return Response(recipe_serializer.data)
            else:
                print(recipe_serializer.errors)
                return Response(recipe_serializer.errors)    
        
    recipes= Recipe.objects.all()
    serializer= RecipeSerializer(recipes, many= True)
    response_data= serializer.data
    return Response(response_data)
        
    
@api_view(['GET', 'DELETE', 'PUT'])
def recipe_detail(request, id):
    try:
        recipe= Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return Response(status=404)
    if request.method=="GET":
        recipe= Recipe.objects.get(id=id)
        recipe_serializer=RecipeSerializer(recipe)
        return Response(recipe_serializer.data)
    
    elif request.method=="PUT":
        recipe= Recipe.objects.get(id=id)
        recipe_serializer=RecipeSerializer(recipe, data=request.data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return Response(recipe_serializer.data)
        
        else:
            return Response(recipe_serializer.errors)
        
    
    elif request.method=="DELETE":
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return Response(status= 204)
        
   
    
@api_view(['GET','POST'])   
def product_list(request):
    try:
        products= Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={"detail":"Requested product doesnot exits"})
            
    if request.method =="POST":
        print(request.data)
        product_serializer= ProductSerializer(data=request.data)
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()
            return Response(product_serializer.data)
        else:
            print(product_serializer.errors)
            return Response(product_serializer.errors)    
        
    products= Product.objects.all()
    serializer= ProductSerializer(products, many= True)
    response_data= serializer.data
    return Response(response_data) 
    
     
@api_view(['GET', 'DELETE', 'PUT'])    
def product_detail(request, id):
    try:
         product= Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=404)     
    if request.method=="GET":
        product= Product.objects.get(id=id)
        product_serializer=ProductSerializer(product)
        return Response(product_serializer.data)
    
    elif request.method=="PUT":
        product= Product.objects.get(id=id)
        product_serializer=ProductSerializer(product, data=request.data )
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data , status=201)
        
        else:
            return Response(product_serializer.errors)
        
    
    elif request.method=="DELETE":
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status= 204)
        
    
      
    
    
    
    # data =[
        
    # ]
    
    # for recipe in recipes:
    #     recipe_object={
            
    #         'id':recipe.id,
    #         'title':recipe.title,
    #         'description':recipe.description,
    #         'time_required':recipe.time_required,
            
            
    #     }
    #     print(recipe_object)
    #     data.append(
    #         recipe_object
    #     )
    # print(data)
    # Response_data={
    #     'recipes':data
    # }
    # return Response(Response_data)
        
        
    