from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Course(models.Model):
     title= models.CharField(max_length=100)
     description= models.CharField(max_length=200)
     credit_hr= models.IntegerField()
     
     def __str__(self):
         return self.title + " ("+ str(self.credit_hr)+" Credits)" 
    
    
# class Subject(models.Model):
#     name= models.CharField(max_length=50)
#     def __str__(self):
#        return self.name()
   
   
class Student(models.Model):
     first_name = models.CharField(max_length=30, blank=True)
     last_name = models.CharField(max_length=30)
     id = models.AutoField(primary_key=True)
     
    #  subjects=models.ManyToManyField(Subject)
     
     Course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name= 'Students', null=True, blank=True)
     email = models.EmailField(blank=False )
     phone= models.CharField(max_length=15, null=True, blank=True, )
     gender= (('M', 'Male'), ('F','Female'))
     gender_choice = models.CharField(max_length=1, choices=gender, null=True, blank=True)
     age= models.PositiveIntegerField(null=True, blank=True)
     image = models.ImageField(upload_to='images/', blank=True, null=True) 
     
     date_joined = models.DateTimeField(auto_now_add=True)
     def  get_full_name(self):
         return f'{self.first_name} {self.last_name}'
     def __str__(self):
         return self.get_full_name()

   
    
