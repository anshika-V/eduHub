from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
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
