from django.shortcuts import render

# Create your views here.


def CreateTest(request, key):
    return render(request, 'material/create-test/build/index.html')


def InstructorPortal(request):
    return render(request, 'material/instructor-portal/build/index.html')
