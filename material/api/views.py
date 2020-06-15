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
def NewTest(request):
    if (request.method == 'POST'):
        test = Test(instructor=request.user,
                    title=request.POST['title'], description=request.POST['description'])
        try:
            test.save()
            return HttpResponse('success ' + str(test.pk))
        except:
            pass
    return render(request, 'material/csrf_token.html')


@login_required
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
def AllTestData(request, key):
    user = request.user
    test = None
    try:
        test = Test.objects.get(pk=int(key))
    except:
        return HttpResponseNotFound('Error: test not found')
    if (test.instructor != user):
        return HttpResponseForbidden('Unauthorised Access: You are not the instructor of requested test')
    json_test_data = serializers.serialize(
        'json', [test],  use_natural_foreign_keys=True)
    json_test_data = json.loads(json_test_data)[0]
    questions = test.question_set.all()
    question_data = serializers.serialize('json', questions)
    question_data = json.loads(question_data)
    json_test_data['questions'] = question_data
    response_data = json.dumps(json_test_data)
    return HttpResponse(response_data, content_type='json_comment_filtered')


@login_required
@csrf_exempt
def SaveTestResponse(request, key):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        data = request.POST['response']
        res = TestResult(
            student=user, parent_test=Test.objects.get(pk=key), questions=data)
        res.save()
        return HttpResponse('saved')
    else:
        return HttpResponseForbidden('Wrong request type')


@login_required
def TestResponses(request, key):
    test = Test.objects.get(pk=key)
    res = test.testresult_set.all()
    data = serializers.serialize(
        'json', res, fields=['student', 'time'], use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='json_comment_filtered')


@login_required
def TestResponseData(request, key):
    data = TestResult.objects.get(pk=key)
    data = serializers.serialize('json', [data])
    return HttpResponse(data, content_type='json_comment_filtered')


@csrf_exempt
@login_required
@allow_instructor
def CheckSaveTestResult(request, key):
    res = TestResult.objects.get(pk=key)
    res.questions = request.POST['data']
    res.checked = True
    res.save()
    return HttpResponse('Saved')


@csrf_exempt
@login_required
@allow_instructor
def DeleteTest(request, key=None):
    if request.method == 'POST':
        test = Test.objects.get(pk=key)
        test.delete()
        return HttpResponse('success')
    return HttpResponse('This test and all releated data will be deleted permanantly')
