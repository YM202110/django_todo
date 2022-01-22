from django.contrib import admin
from .models import Todo, TodoCategory, TodoStatus

# Register your models here.
admin.site.register(Todo)
admin.site.register(TodoCategory)
admin.site.register(TodoStatus)