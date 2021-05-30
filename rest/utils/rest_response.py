import json

from django.core import serializers
from django.db.models import QuerySet
from django.http import HttpResponse


def rest_response(model_data, fields=None):
    if type(model_data) is not QuerySet:
        data = serializers.serialize('json', [model_data, ])
        struct = json.loads(data)
        data = json.dumps(struct[0])
    else:
        data = serializers.serialize('json', model_data, fields=fields)
    return HttpResponse(
        data,
        content_type='application/json'
    )
