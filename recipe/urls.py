
from django.urls import path, include
from recipe import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'recipeviewset', views.RecipeViewSet, basename='recipeviewset') 
router.register(r'productviewset', views.ProductViewSet, basename='productviewset')


urlpatterns = [
    path('hello/', views.hello),
    path('list_recipes/', views.list_recipe),
    path('recipes/<int:id>/', views.recipe_detail),
    path('product/', views.product_list),
    path('product/<int:id>/', views.product_detail),
    path('api/', include(router.urls)),
    path('recipe_c/', views.RecipeListView.as_view()),
   
]
