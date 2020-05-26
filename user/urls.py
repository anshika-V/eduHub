from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginType, name='login type'),
    path('login/student/', views.CustomLogin.as_view(success_url='/',
                                                     type='S'), name="student login"),
    path('login/instructor/', views.CustomLogin.as_view(success_url='/',
                                                        type='I'), name="instructor login"),
    path('signup/', views.RegisterType, name="register type"),
    path('signup/student/', views.Register.as_view(success_url='/user/signup/ps'),
         name='student register'),
    path('signup/instructor/', views.Register.as_view(success_url='/user/signup/pi'),
         name='instructor register'),
    path('signup/ps/',
         login_required(views.ProfileUpdate.as_view(initial={'type': 'S'}))),
    path('signup/pi/',
         login_required(views.ProfileUpdate.as_view(initial={'type': 'I'})))

]
