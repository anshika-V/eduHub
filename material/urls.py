from django.urls import path, include
from . import views
urlpatterns = [
    path('api/', include('material.api.urls')),
    path('create-test/<int:key>/', views.CreateTest),
    path('instructor-portal/', views.InstructorPortal)
]
