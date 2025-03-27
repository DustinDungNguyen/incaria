from django.shortcuts import render, HttpResponse
from .models import TodoItem

#Connect to html file of the database design.
def home(request):
    return render(request,"home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos" : items})

