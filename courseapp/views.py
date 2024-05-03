from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer,CourseListSerializer,StudentListSerializer
from rest_framework.views  import APIView
from django.shortcuts import get_object_or_404

# Create your views here.


class CourseListView(APIView):
    
     def get(self, request):
         title= request.query_params.get('title')
         print(title)
         if title is not None:
             courses = Course.objects.filter(title__icontains=title)
         else:
             courses = Course.objects.all()

         serializer= CourseListSerializer(courses, many=True)
         return Response(serializer.data)
    
     def post(self,request):
         course_serializer=CourseListSerializer(data=request.data)
         course_serializer.is_valid(raise_exception=True)
         course_serializer.save()
         return Response(course_serializer.data,status=201)
    
    
class CourseDetailView(APIView):
     
     def get(self, request, *args, **kwargs):
         id = kwargs.get("id")
         print(id)
         try:
             course = Course.objects.get(id=id)
         except Course.DoesNotExist:
                 return Response({
                     "msg": "This Course  does not exist"
                 }, status=404)
           
         if request.method == 'GET':
             course_serializer = CourseListSerializer(course)
             return Response(course_serializer.data)   



class StudentListView(APIView):
    
     def get(self, request):
         first_name= request.query_params.get('first_name')
         print(first_name)
         if first_name is not None:
             students = Student.objects.filter(name__icontains=first_name)
         else:
             students = Student.objects.filter()

         serializer= StudentSerializer(students, many=True)
         return Response(serializer.data)
    
     def post(self,request):
         student_serializer=StudentListSerializer(data=request.data)
         student_serializer.is_valid(raise_exception=True)
         student_serializer.save()
         return Response(student_serializer.data,status=201)        
     
     
class DisplayStudentView(APIView):
     http_method_names=['GET']
     
     def get(self,request ) :
          user = request.user
          #print (user)
          
          if isinstance(user,Student):
               student_info = Student.objects.filter(student_id=user)  
               
               data={}
               data["first_name"]=user.first_name
               data["last_name"]=user.last_name
               data["Email"]=user.email
               data["phone"]=user.phone
               data["gender"]=user.gender
               data["age"]=user.age
               data["Course"]=user.Course
               data["image"]=user.image
            
            
               
               

              
          
          
          