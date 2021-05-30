import json

from django.utils.deprecation import MiddlewareMixin


class BodyParserMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if request.body:
            request_data = getattr(request, '_body', request.body)
            request._body = json.loads(request_data)
        return None
