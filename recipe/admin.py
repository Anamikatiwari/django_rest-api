from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import RecipeResource


# Register your models here.


class Recipeadmin(ImportExportModelAdmin):
    resource_classes= [RecipeResource]
    list_display = ('title', 'description', 'time_required')
    search_fields=('title',)
    list_filter=('user',)
    
admin.site.register(Recipe, Recipeadmin)
admin.site.register(Ingredient)

admin.site.register(Product)