from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from user.decorators import allow_instructor
from django.core import serializers
from django.shortcuts import render
from material.models import Test
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
    tests = user.test_set.all()
    tests = serializers.serialize('json', tests)
    tests = json.loads(tests)
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
    json_test_data = serializers.serialize('json', [test])
    json_test_data = json.loads(json_test_data)[0]
    questions = test.question_set.all()
    question_data = serializers.serialize('json', questions)
    question_data = json.loads(question_data)
    json_test_data['questions'] = question_data
    response_data = json.dumps(json_test_data)
    return HttpResponse(response_data, content_type='json_comment_filtered')
