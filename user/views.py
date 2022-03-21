from rest_framework.viewsets import GenericViewSet
from .serializers import UserModelSerializer
from .models import User
from rest_framework import mixins


class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
