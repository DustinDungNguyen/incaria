from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .models import User

#Connect to html file of the database design.
def home(request):
    return render(request,"home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos" : items})

def incaria(request):
    # Query all users
    users = User.objects.all()
    return render(request, 'incaria.html', {'users': users})
