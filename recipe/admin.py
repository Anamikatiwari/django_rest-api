from django.contrib import admin
from .models import *


# Register your models here.


class Recipeadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_required')
    search_fields=('title',)
    list_filter=('user',)
    
admin.site.register(Recipe, Recipeadmin)
admin.site.register(Ingredient)

admin.site.register(Product)