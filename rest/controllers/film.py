from django.views.decorators.http import require_http_methods

from rest.utils import filter_model
from rest.utils import rest_response
from rest.models import Film


@require_http_methods(["GET"])
def get_all(request):
    films = filter_model(Film, request.GET, custom_filters={
        'releaseDate__year': 'year'
    })
    return rest_response(films)


@require_http_methods(["GET"])
def index_at(request, film_id):
    film = Film.objects.get(id=film_id)
    return rest_response(film)
