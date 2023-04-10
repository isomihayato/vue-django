from django.shortcuts import render
from django.http import JsonResponse
from .models import ToDoItems
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def get_todo_items(request):
    items = ToDoItems.objects.all()
    todo_items = []
    for item in items:
        todo_items.append ({
            'id': item.id,
            'text': item.text,
            'done': item.done
        })
    return JsonResponse(todo_items, safe=False)

def create_task(request):
    serializer = TaskSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)