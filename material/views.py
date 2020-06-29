from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.decorators import allow_instructor
from .models import Test, TestResult
from django.http import HttpResponseForbidden, HttpResponseBadRequest

# Create your views here.


@login_required
@allow_instructor
def InstructorPortal(request):
    return render(request, 'material/instructor-portal/build/index.html')


@login_required
@allow_instructor
def InstructorPortalTest(request):
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
    test = Test.objects.get(pk=int(key))
    user = request.user
    # bool value for i user have already attempted the test
    testResults = user.testresult_set.all().filter(parent_test=test)
    attempted = testResults.exists()
    if (attempted):  # if already attempted return the page showing laready attempted
        dic = {'title': 'Result', 'test_title': test.title,
               'instructor': test.instructor.username, 'pk': testResults[0].pk}
        return render(request, 'material/TestAttempted.html', dic)
    if (test.access == 1):  # if access for test is private
        dic = {'title': 'Private Test', 'test_title': test.title,
               'instructor': test.instructor.username, 'time': test.duration}
        if (request.method == 'POST'):
            # Return the test page of user provides teh write access key
            if (request.POST['key'] == test.accessKey):
                return render(request, 'material/student-test/build/index.html')
            else:
                # Error message for invalid access key
                dic.update({'msga': 'Invalid Access Key'})
        # page to write access key
        return render(request, 'material/TestAuth.html', dic)
    return render(request, 'material/student-test/build/index.html')


@login_required
@allow_instructor
def CreateTestSeries(request, key):
    return render(request, 'material/create-test-series/build/index.html')


@login_required
@allow_instructor
def InstructorPortalTestSeries(request):
    return render(request, 'material/instructor-portal-testSeries/build/index.html')


@login_required
def TestResultStudent(request, key):
    testResult = None
    try:
        testResult = TestResult.objects.get(pk=int(key))
        # if requesting user is not the student of test result
        if (testResult.student != request.user):
            return HttpResponseForbidden('Unauthorised Access')
    except:
        # when requested pk is not found
        return HttpResponseBadRequest('Not Found')
    return render(request, 'material/test-result/build/index.html')
