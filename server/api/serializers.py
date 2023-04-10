from rest_framework import serializers
from .models import ToDoItems

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItems
        fields= '__all__'