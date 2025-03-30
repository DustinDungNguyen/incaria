from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
    path("incaria/", views.incaria, name="incaria"),  # new URL for Incaria view
]