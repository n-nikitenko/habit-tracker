from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from habits.models import Habit
from habits.validators import (validate_exec_time, validate_periodicity,
                               validate_related_pleasant_habit)


class HabitSerializer(serializers.ModelSerializer):
    execution_time = serializers.IntegerField(
        validators=[validate_exec_time], required=False
    )
    periodicity = serializers.IntegerField(
        validators=[validate_periodicity], required=False
    )
    related_pleasant_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.all(),
        validators=[validate_related_pleasant_habit],
        required=False,
    )

    def validate(self, data):
        # Исключить одновременный выбор связанной привычки и указания вознаграждения
        related_pleasant_habit = data.get("related_pleasant_habit")
        if data.get("reward") and related_pleasant_habit:
            raise ValidationError(
                "Не допустим одновременный выбор связанной привычки и указание вознаграждения"
            )
        #    У приятной привычки не может быть вознаграждения или связанной привычки
        if data.get("is_pleasant") and (data.get("reward") or related_pleasant_habit):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
            )
        return data

    class Meta:
        model = Habit
        fields = "__all__"
