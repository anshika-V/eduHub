
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginType, name='login_type'),
]
