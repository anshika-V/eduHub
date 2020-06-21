from django.urls import path
from . import views

urlpatterns = [
    path('newTest/', views.NewTest),
    path('newTestSeries/', views.NewTestSeries),
    path('instructor-dashboard-data/', views.InstructorDashboardData),
    path('instructor-portal/test/', views.InstructorPortalTest),
    path('instructor-portal/testSeries/', views.InstructorPortalTestSeries),
    path('test/data/<int:key>/', views.AllTestData),
    path('test/saveResponse/<int:key>/', views.SaveTestResponse),
    path('test/response/<int:key>/', views.TestResponses),
    path('test/responseData/<int:key>/', views.TestResponseData),
    path('test/responseData/checkSave/<int:key>/', views.CheckSaveTestResult),
    path('test/deleteTest/<int:key>/', views.DeleteTest),
    path('testS/deleteTestSeries/<int:key>/', views.DeleteTestSeries)
]
