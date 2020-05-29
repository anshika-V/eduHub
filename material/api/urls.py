from django.urls import path
from . import views

urlpatterns = [
    path('newTest/', views.NewTest),
    path('instructor-dashboard-data/', views.InstructorDashboardData)
]
