from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectModelSerializer, TodoModelSerializer
from .models import Project, Todo


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()


class TodoViewSet(ModelViewSet):
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()
