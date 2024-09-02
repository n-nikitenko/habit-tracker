from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    """проверка, является ли пользователь автором привычки."""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsPublicPermission(permissions.BasePermission):
    """проверка, является ли  привычка публичной."""

    def has_object_permission(self, request, view, obj):
        return obj.is_public
