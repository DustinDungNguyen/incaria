from django.contrib import admin
from .models import User, Category, Condition, TodoItem


# Register your models here.
admin.site.register(TodoItem)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Condition)
