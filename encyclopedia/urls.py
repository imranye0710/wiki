from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("<str:title>", views.entry, name="title"),
]
