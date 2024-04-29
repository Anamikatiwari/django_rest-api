from django.db import models

# Create your models here.
class Recipe(models.Model):
    title= models.CharField(max_length = 200)
    description = models.TextField()
    time_required= models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    
   
    
class Product(models.Model):
    name= models.CharField(max_length=100)   
    description= models.TextField(blank=True, null=True)
    quantity= models.PositiveIntegerField()
    price= models.DecimalField(max_digits=20, decimal_places=2)
    expiry_date= models.DateField()
    

    def __str__(self):
     return self.name