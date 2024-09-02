from django.shortcuts import get_object_or_404
from rest_framework.serializers import ValidationError

from habits.models import Habit


def validate_exec_time(value):
    """Проверка, что значение времени выполнения не больше 120 секунд"""

    if value < 1:
        raise ValidationError(
            "Значение времени выполнения привычки должно быть положительным числом в секундах"
        )
    if value > 120:
        raise ValidationError(
            "Значение времени выполнения привычки должно быть не больше 120 секунд"
        )


def validate_periodicity(value):
    """Проверка, что значение периодичности выполнения привычки не больше 7 дней"""
    if value < 1:
        raise ValidationError(
            "значение периодичности выполнения привычки должно быть не менее 1 дня"
        )
    if value > 7:
        raise ValidationError(
            "значение периодичности выполнения привычки должно быть не больше 7 дней"
        )


def validate_related_pleasant_habit(value):
    """Проверка, что в связанные привычки попадают только привычки с признаком приятной привычки."""

    if not value.is_pleasant:
        raise ValidationError(
            "В связанные привычки можно добавлять только привычки с признаком приятной привычки"
        )
