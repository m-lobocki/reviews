from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from rest.decorators import logged
from rest.utils import rest_response, filter_model, merge_body_model
from rest.models import Review, Film


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "GET":
        return _get_all(request)
    elif request.method == "POST":
        return _add(request)


@logged
def _add(request):
    film = Film.objects.get(id=request.body['filmId'])
    review = Review(author=request.user, film=film, rating=request.body['rating'], text=request.body['text'])
    review.save()
    return rest_response(review)


def _get_all(request):
    films = filter_model(Review, request.GET)
    return rest_response(films)


@require_http_methods(["GET", "PUT", "DELETE"])
def index_at(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == "GET":
        return _get(request, review)
    elif request.method == "PUT":
        return _update(request, review)
    elif request.method == "DELETE":
        return _delete(request, review)


@require_http_methods(["GET"])
def get_all(request):
    films = filter_model(Film, request.GET)
    return rest_response(films)


def _get(request, review):
    return rest_response(review)


@logged
def _update(request, review):
    result = merge_body_model(request.body, review)
    return rest_response(result)


@logged
def _delete(request, review):
    review.delete()
    return HttpResponse()
