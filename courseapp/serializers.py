from rest_framework import serializers
from .models import Course, Student

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # fields= [
        #     "title", "description"
        # ]   
        fields= [
            'title',
            'description',
            'credit_hr',
        ]


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields= '__all__'
        
        
class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields= [
        #     "title", "description"
        # ]   
        fields= [
            'first_name',
            'last_name', 
            'email',
            'phone',
            'gender',
            'age',
            'Course',
            'image',
        ]
       
        
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields= '__all__'
                