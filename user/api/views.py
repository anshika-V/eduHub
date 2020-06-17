from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
import json


@login_required
def ProfileData(request):  # send all profile data
    user = request.user
    profile = user.profile
    json_data = serializers.serialize('json', [profile])
    json_data = json.loads(json_data)[0]
    del json_data['model']
    json_data['username'] = user.username
    json_data['email'] = user.email
    json_data['name'] = user.first_name
    json_data = json.dumps(json_data)
    return HttpResponse(json_data, content_type='json_comment_filtered')
