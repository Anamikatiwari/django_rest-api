from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Recipe, Product
from rest_framework.viewsets import ModelViewSet
from .serializers import RecipeSerializer, ProductSerializer,RecipeListSerializer,RecipeCreateSerializer
from rest_framework.views  import APIView
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class RecipeViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer 


class ProductViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class RecipeListView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        title= request.query_params.get('title')
        print(title)
        if title is not None:
            recipes = Recipe.objects.filter(title__icontains=title, user= request.user)
        else:
            recipes = Recipe.objects.filter(user=request.user)

        serializer= RecipeListSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        recipe_serializer=RecipeCreateSerializer(data=request.data)
        recipe_serializer.is_valid(raise_exception=True)
        recipe_serializer.save(user=request.user)
        return Response(recipe_serializer.data,status=201)
        
    
    
        
class RecipeDetailView(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        print(id)
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
                return Response({
                    "msg": "No such recipe exists"
                }, status=404)
                    
            
        serializer= RecipeSerializer(recipe)
        return Response(serializer.data)  
    
    def put(self,request,*args,**kwargs):
        id=self.kwargs.get('id')
        recipe=Recipe.objects.get(id=id)
        recipe_serializer=RecipeSerializer(recipe,data=request.data)
        if recipe_serializer.is_valid():
            recipe_serializer.save(updated_by=request.user)
            return Response(recipe_serializer.data)
        else:
            print(recipe_serializer.errors)
            return Response(recipe_serializer.errors)
        
    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        try:
            recipe=Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response(status=404)
        recipe.delete()
        return Response(status=204)
    




@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def hello(request):
    return Response({
        "data": "Hello, world!"
    })
    
     
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def list_recipe(request):
    if request.method=='POST':
        print(request.data)
        recipe_serializer=RecipeCreateSerializer(data=request.data)
        
        if recipe_serializer.is_valid(raise_exception=True):
            recipe_serializer.save(user=request.user)
            # validated_data=recipe_serializer.validated_data
            # recipe=Recipe(user=request.user,**validated_data)
            # recipe.save()
            # recipe_serializer=RecipeCreateSerializer(recipe)
            return Response(recipe_serializer.data,status=201)     
        else:
            print(recipe_serializer.errors)
            return Response(recipe_serializer.errors)
    
    recipes=Recipe.objects.all()
    serializer=RecipeSerializer(recipes,many=True)
    return Response(serializer.data,status=201)


        
    
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
        
        
    