from functools import wraps

from django.http import HttpResponseForbidden


def logged(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return HttpResponseForbidden()

    return decorator
