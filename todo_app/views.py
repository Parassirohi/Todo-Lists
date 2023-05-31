from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication

from .serializer import TaskSerializer, TagSerializer
from .models import Task, Tag
from .pagination import DefaultPagination


class TaskViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    pagination_class = DefaultPagination
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        # Extract and process tags separately
        tags_data = self.request.data.pop('tags', None)
        task = serializer.save()

        # Process tags and add them to the task
        if tags_data:
            tags = []
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                tags.append(tag)
            task.tags.set(tags)
            task.save()


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

