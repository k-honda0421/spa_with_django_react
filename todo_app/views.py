from django.shortcuts import render
from rest_framework import filters, generics, viewsets

from .models import Todo
from .serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    fileter_fields = ("name",)
