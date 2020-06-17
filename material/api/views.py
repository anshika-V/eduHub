from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from user.decorators import allow_instructor
from django.core import serializers
from django.shortcuts import render
from material.models import Test, TestResult
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


@login_required  # Provides all data of the instructor dashboard add other data as the projects goes on
def InstructorDashboardData(request):
    user = request.user
    testsObj = user.test_set.all()
    tests = serializers.serialize('json', testsObj)
    tests = json.loads(tests)
    i = 0
    for tes in testsObj:
        l = len(tes.testresult_set.all())
        tests[i]['attempts'] = l
        i = i+1
    data = {'tests': tests}
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
