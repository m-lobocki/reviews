from django.urls import path
from . import controllers

urlpatterns = [
    path('user/login', controllers.user.login),
    path('user/logout', controllers.user.logout),
    path('user/register', controllers.user.register),
    path('user', controllers.user.index),
    path('user/change-password', controllers.user.change_password),
    path('film/<int:film_id>', controllers.film.index_at),
    path('film', controllers.film.get_all),
    path('review/<int:review_id>', controllers.review.index_at),
    path('review', controllers.review.index),
    path('person/<int:person_id>', controllers.person.index_at),
    path('person', controllers.person.index),
]
