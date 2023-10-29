from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<str:page>", views.index),
    path("services/bakery", views.bakery, name="bakery"),
    path("services/bakery/<str:other_args>", views.bakery),
    path("<str:page>/<str:subpage>", views.index),
    path("<str:page>/<str:subpage>/<str:other_args>", views.index),
]