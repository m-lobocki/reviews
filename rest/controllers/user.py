from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponseForbidden, HttpResponse
from django.views.decorators.http import require_http_methods

from decorators import logged


@require_http_methods(["POST"])
def login(request):
    user = authenticate(request, username=request.body['email'], password=request.body['password'])
    if user is not None:
        django_login(request, user)
        return HttpResponse()
    else:
        return HttpResponseForbidden()


@logged
@require_http_methods(["POST"])
def logout(request):
    django_logout(request)
    return HttpResponse()


@require_http_methods(["POST"])
def register(request):
    User.objects.create_user(request.body['email'], request.body['email'], request.body['password'])
    return HttpResponse()


@require_http_methods(["POST"])
def change_password(request):
    user = User.objects.get(email=request.body['email'])
    if user.check_password(request.body['oldPassword']):
        user.set_password(request.body['newPassword'])
        user.save()
        return HttpResponse()
    return HttpResponseForbidden()


@logged
@require_http_methods(["DELETE"])
def index(request: HttpRequest):
    request.user.delete()
    return HttpResponse()
