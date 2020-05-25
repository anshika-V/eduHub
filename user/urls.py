from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginType, name='login_type'),
    path('login/student/', views.CustomLogin.as_view(success_url='/',
                                                     template_name='user/registration.html', extra_context={'title': 'Login'}, redirect_authenticated_user=True), name="student login"),
    path('login/instructor/', views.CustomLogin.as_view(success_url='/', template_name='user/registration.html',
                                                        extra_context={'title': 'Login'}, redirect_authenticated_user=True), name="student login"),
    path('student/signup/', views.Register.as_view(success_url='/user/signup/ps'),
         name='student register'),
    path('instructor/signup/', views.Register.as_view(success_url='/user/signup/pi'),
         name='instructor register'),
    path('signup/ps/', views.ProfileUpdate.as_view(initial={type: 'S'})),
    path('signup/pi/', views.ProfileUpdate.as_view(initial={'type': 'I'}))

]
