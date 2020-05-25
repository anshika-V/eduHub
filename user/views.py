from django.shortcuts import render

# Create your views here.


def LoginType(request):
    return render(request, 'user/login_type.html', {'title': 'Login'})
