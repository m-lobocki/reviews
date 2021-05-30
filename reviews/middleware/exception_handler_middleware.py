from django.db import IntegrityError
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class ExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if len(exception.args) == 1:
            error = {'code': -1, 'reason': exception.args[0]}
        elif len(exception.args) == 2:
            code, reason = exception.args
            error = {'code': code, 'reason': reason}
        else:
            error = {'code': -1, 'reason': 'unknown'}
        status = 400
        if type(exception) is IntegrityError:
            status = 409
        return JsonResponse(error, status=status)
