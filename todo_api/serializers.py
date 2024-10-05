from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.filters import OrderingFilter

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description"]
        read_only_fields = ['id']
        filter_backends = (DjangoFilterBackend, OrderingFilter)
        ordering_fields = ['title', 'description']
        ordering = ['title', 'description']