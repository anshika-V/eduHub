from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from user.decorators import allow_instructor
from django.core import serializers
from django.shortcuts import render
from material.models import Test, TestResult, TestSeries
from .serializers import TestSeriesSerializer
import json


@csrf_exempt
@login_required
def NewTest(request):  # form for creating new test, this is csrf safe af i am sending csrf token can remove @csrf_exempt in production
    if (request.method == 'POST'):
        test = Test(instructor=request.user,
                    title=request.POST['title'], description=request.POST['description'])
        try:
            test.save()
            return HttpResponse('success ' + str(test.pk))
        except:
            pass
    return render(request, 'material/csrf_token.html')


@csrf_exempt
@login_required
def NewTestSeries(request):  # form for creating new test series, this is csrf safe af i am sending csrf token can remove @csrf_exempt in production
    if (request.method == 'POST'):
        testSeries = TestSeries(instructor=request.user,
                                title=request.POST['title'], description=request.POST['description'])
        try:
            testSeries.save()
            return HttpResponse('success ' + str(testSeries.pk))
        except:
            pass
    return render(request, 'material/csrf_token.html')


@login_required  # Provides all data of the instructor dashboard add other data as the projects goes on
def InstructorDashboardData(request):
    user = request.user
    testsObj = user.test_set.all()
    testSeriesObjs = user.testseries_set.all()
    data = {'tests': len(testsObj), 'courses': 0, 'blogs': 0,  # length of all model obetcs owned by user
            'testSeries': len(testSeriesObjs)}
    data = json.dumps(data)
    return HttpResponse(data, content_type="json_comment_filtered")


@login_required
@allow_instructor
def InstructorPortalTest(request):
    user = request.user
    testsObj = user.test_set.all()
    # all tests owned by the user
    tests = serializers.serialize('json', testsObj)
    tests = json.loads(tests)
    i = 0
    for tes in testsObj:
        l = len(tes.testresult_set.all())  # all responses submitted by student
        tests[i]['attempts'] = l
        i = i+1
    data = json.dumps(tests)
    return HttpResponse(data, content_type="json_comment_filtered")


@login_required
@allow_instructor
def InstructorPortalTestSeries(request):
    user = request.user
    testSeriesObjs = user.testseries_set.all()  # all test series owned by the user
    data = serializers.serialize(
        'json', testSeriesObjs, fields=['title', 'time', 'access'])
    data = json.loads(data)
    i = 0
    for d in data:
        # all test series responses submited by student
        l = len(testSeriesObjs[i].testseriesresponse_set.all())
        d['attempts'] = l
        i += 1
    data = json.dumps(data)
    return HttpResponse(data, content_type="json_comment_filtered")


@login_required
@allow_instructor
def AllTestData(request, key):  # Returns all data releated to a particular test
    user = request.user
    test = None
    try:
        test = Test.objects.get(pk=int(key))
    except:
        return HttpResponseNotFound('Error: test not found')
    if (test.instructor != user):  # Checking if requesting user is the instructor of the requested test
        return HttpResponseForbidden('Unauthorised Access: You are not the instructor of requested test')
    json_test_data = serializers.serialize(
        'json', [test],  use_natural_foreign_keys=True)
    json_test_data = json.loads(json_test_data)[0]
    questions = test.question_set.all()
    question_data = serializers.serialize('json', questions)
    question_data = json.loads(question_data)
    # Adding all theh questions of the test in the response
    json_test_data['questions'] = question_data
    response_data = json.dumps(json_test_data)
    return HttpResponse(response_data, content_type='json_comment_filtered')


@login_required
@csrf_exempt  # Thsi is possibily not csrf safe, make it safe in upcoming iteration
def SaveTestResponse(request, key):  # Save the response of a student who submitted a test
    if request.method == 'POST':
        user = request.user
        data = request.POST['response']
        res = TestResult(
            student=user, parent_test=Test.objects.get(pk=key), questions=data)
        res.save()
        return HttpResponse('saved')
    else:
        return HttpResponseForbidden('Wrong request type')


@login_required
def TestResponses(request, key):  # Summary data of a All The test response of a particular test
    test = Test.objects.get(pk=key)
    # Checking if requesting user is the instructor of the requested test
    if (test.instructor != request.user):
        return HttpResponseForbidden('Unauthorised Access: You are not the instructor of requested test')
    res = test.testresult_set.all()
    data = serializers.serialize(
        'json', res, fields=['student', 'time'], use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='json_comment_filtered')


@login_required
def TestResponseData(request, key):  # Test response data of a particular test response
    res = TestResult.objects.get(pk=key)
    test = res.parent_test
    # Checking if requesting user is the instructor of the requested test result test
    if (test.instructor != request.user):
        return HttpResponseForbidden('Unauthorised Access: You are not the instructor of requested test')
    data = serializers.serialize('json', [res])
    return HttpResponse(data, content_type='json_comment_filtered')


@csrf_exempt  # Possibily Not secure make it in next iteration
@login_required
@allow_instructor   # For saving the updated test response link marks and remarks
def CheckSaveTestResult(request, key):
    res = TestResult.objects.get(pk=key)
    res.questions = request.POST['data']
    res.checked = True
    res.save()
    return HttpResponse('Saved')


@csrf_exempt  # Possibily Not secure make it in next iteration
@login_required
@allow_instructor
def DeleteTest(request, key=None):  # for deleting a test
    if request.method == 'POST':
        test = Test.objects.get(pk=key)
        test.delete()
        return HttpResponse('success')
    return HttpResponse('This test and all releated data will be deleted permanantly')


@csrf_exempt  # Possibily Not secure make it in next iteration
@login_required
@allow_instructor
def DeleteTestSeries(request, key=None):  # for deleting a testSeries
    if request.method == 'POST':
        testS = TestSeries.objects.get(pk=key)
        testS.delete()
        return HttpResponse('success')
    return HttpResponse('This test and all releated data will be deleted permanantly')


@login_required
@allow_instructor
# all data of a particular test series
def CreateTestSeriesData(request, key=None):
    user = request.user
    testSeries = None
    testObj = None
    try:
        testSeries = TestSeries.objects.get(pk=int(key))
        testObj = user.test_set.all()
    except:
        return HttpResponseNotFound('Error: test series not found')
    # Checking if requesting user is the instructor of the requested testSeries
    if (testSeries.instructor != user):
        return HttpResponseForbidden('Unauthorised Access: You are not the instructor of requested test')
    json_testSeries_data = serializers.serialize(
        'json', [testSeries])
    json_test_list = serializers.serialize(
        'json', testObj, use_natural_foreign_keys=True)
    json_testSeries_data = json.loads(json_testSeries_data)
    json_test_list = json.loads(json_test_list)
    response_data = {'testSeries': json_testSeries_data[0],
                     'testList': json_test_list}
    response_data = json.dumps(response_data)
    return HttpResponse(response_data, content_type='json_comment_filtered')


@login_required
@allow_instructor
# all data of a particular test series for student portal
def StudentTestSeriesData(request, key=None):
    user = request.user
    testSeries = None
    try:
        testSeries = TestSeries.objects.get(pk=int(key))
    except:
        return HttpResponseNotFound('Error: test series not found')
    json_testSeries = TestSeriesSerializer(testSeries)
    # dumps data into json striing and then sends it as response
    return JsonResponse(json_testSeries.data)


@csrf_exempt
@login_required
@allow_instructor
def SaveTestSeriesData(request):
    if (request.method == 'GET'):
        return HttpResponseBadRequest('Invalid Request')
    try:
        data = serializers.deserialize('json', request.POST['data'])
        for obj in data:
            obj.save()
    except:
        return HttpResponseBadRequest('Invalid Request: Wrogly formatted data')
    return HttpResponse('success')
