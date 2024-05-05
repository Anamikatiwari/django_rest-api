
from django.urls import path, include
from courseapp import views


urlpatterns = [
    
     path('courses/', views.CourseListView.as_view()),
     path('courses/<int:id>', views.CourseDetailView.as_view()),
     path('students/',views.StudentListView .as_view()),
     path('studentbycourse/<int:id>', views.DisplayStudentView.as_view()),
     path('students_p/', views.StudentListAPIView.as_view())
    
]

