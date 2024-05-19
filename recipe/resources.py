from import_export import resources
from .models import Recipe


class RecipeResource(resources.ModelResource):
    class Meta:
        model= Recipe
        field=('id','ingredients','title', 'description','difficulty','rating','user__username')