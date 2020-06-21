from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.decorators import allow_instructor

# Create your views here.


@login_required
@allow_instructor
def InstructorPortal(request):
    return render(request, 'material/instructor-portal/build/index.html')


@login_required
@allow_instructor
def InstructotPortalTest(request):
    return render(request, 'material/instructor-portal-test/build/index.html')


@login_required
@allow_instructor
def CreateTest(request, key):
    return render(request, 'material/create-test/build/index.html')


@login_required
@allow_instructor
def CheckTest(request, key):
    return render(request, 'material/check-test/build/index.html')


@login_required
def StudentTest(request, key):
    return render(request, 'material/student-test/build/index.html')
