from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsAuthorPermission, IsPublicPermission
from habits.serializers import HabitSerializer


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(operation_description="Получение списка привычек авторизованного пользователя"),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(operation_description="Создание привычки"),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Получение данных привычки по id"
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_description="Обновление данных привычки по id"
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(operation_description="Удаление привычки по id"),
)
@method_decorator(
    name="public_list",
    decorator=swagger_auto_schema(operation_description="Список публичных привычек"),
)
class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    queryset = Habit.objects.all()

    @action(["GET"], url_path=r"publics", name="publics", detail=False)
    def public_list(self, request):
        queryset = Habit.objects.filter(is_public=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = Habit.objects.filter(Q(author=self.request.user) | Q(is_public=True))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ["create", "update", "delete"]:
            self.permission_classes = (
                IsAuthenticated,
                IsAuthorPermission,
            )
        else:
            self.permission_classes = (
                IsAuthenticated,
                IsAuthorPermission | IsPublicPermission,
            )
        return super().get_permissions()
