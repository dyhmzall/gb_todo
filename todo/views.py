from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectModelSerializer, TodoModelSerializer
from .models import Project, Todo
from .paginations import ProjectLimitOffsetPagination, TodoLimitOffsetPagination
from .filters import ProjectFilter
from rest_framework.response import Response


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class TodoViewSet(ModelViewSet):
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
    pagination_class = TodoLimitOffsetPagination
    filterset_fields = ['project']

    def destroy(self, request, pk=None, **kwargs):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Response({"error": "not found"})
        todo.status = False
        todo.save()
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)
