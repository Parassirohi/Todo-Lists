from rest_framework import serializers

from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        read_only_field = ('timestamp', 'tags')
        model = Task
        fields = ('id', 'timestamp', 'title', 'description', 'due_date', 'tags', 'status')

