from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title= models.CharField(max_length = 200)
    description = models.TextField()
    time_required= models.CharField(max_length=20)
    difficulty= models.CharField(max_length=20,  null=True, blank=True) 
    rating=models.FloatField(null=True, blank=True) 
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name= 'updated_by')   
    updated_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name= 'created_by')  
    
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