from django.urls import path, include
from . import views
urlpatterns = [
    path('api/', include('material.api.urls')),
    path('create-test/<int:key>/', views.CreateTest, name="create-test"),
    path('instructor-portal/', views.InstructorPortal, name='instructor-portal'),
    path('student-test/<int:key>/', views.StudentTest, name="student-test"),
    path('check-test/<int:key>/', views.CheckTest, name="check-test")
]
