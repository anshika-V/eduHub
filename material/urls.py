from django.urls import path, include
from . import views
urlpatterns = [
    path('api/', include('material.api.urls')),
    path('create-test/<int:key>/', views.CreateTest, name="create-test"),
    path('create-test-series/<int:key>/',
         views.CreateTestSeries, name="create-test-series"),
    path('instructor-portal/', views.InstructorPortal, name='instructor-portal'),
    path('instructor-portal/test/', views.InstructorPortalTest),
    path('student-test/<int:key>/', views.StudentTest, name="student-test"),
    path('check-test/<int:key>/', views.CheckTest, name="check-test"),
    path('instructor-portal/test-series/', views.InstructorPortalTestSeries),
    path('test-result/<int:key>/', views.TestResultStudent)
]
