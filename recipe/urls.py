
from django.urls import path, include
from recipe import views
from rest_framework.routers import DefaultRouter
from.views import ContactAPIView

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
    path('recipe_c/<int:id>', views.RecipeDetailView.as_view()),
    path('send_mail/', views.mail_user),
    path('contact/',views.handle_contact, name='contact'),

    path('contacts/', ContactAPIView.as_view(), name='contact_api'),
    path('uploadcsv/', views.upload_ingredient_csv, name='upload_ingredient_csv')

   
]
