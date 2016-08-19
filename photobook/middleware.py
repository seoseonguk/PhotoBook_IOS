import json
from django.db.models import Model
from django.db.models.query import QuerySet
from django.http import HttpResponse, QueryDict
from .encoder import DjangoJSONEncoder


class JsonResponseMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, (str, bytes)):
            if response and response[0] in ('"', '[', '{'):
                return HttpResponse(response, content_type='application/json')
            return HttpResponse(response)
        elif isinstance(response, (set, dict, list, tuple, QuerySet, Model)):
            json_string = json.dumps(response, cls=DjangoJSONEncoder, ensure_ascii=False)
            return HttpResponse(json_string, content_type='application/json')
        else:
            return response