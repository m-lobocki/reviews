from django.views.decorators.http import require_http_methods

from models import filter_model
from models.rest_response import rest_response
from rest.models import Person


@require_http_methods(["GET"])
def index(request):
    films = filter_model(Person, request.GET)
    return rest_response(films)


@require_http_methods(["GET"])
def index_at(request, person_id):
    film = Person.objects.get(id=person_id)
    return rest_response(film)
