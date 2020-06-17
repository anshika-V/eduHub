from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileData)  # for profil data
]
