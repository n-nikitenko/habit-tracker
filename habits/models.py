from django.db import models

from config import settings


class Habit(models.Model):
    """модель привычки"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="habits",
        null=True,
        blank=True,
    )

    place = models.CharField(
        max_length=255,
        verbose_name="Место, в котором необходимо выполнять привычку",
        help_text="Место, в котором необходимо выполнять привычку",
    )

    time = models.CharField(
        max_length=255,
        verbose_name="Время, в которое необходимо выполнять привычку",
        help_text="Время, в которое необходимо выполнять привычку",
    )

    action = models.TextField(
        verbose_name="Действие, которое представляет собой привычка",
        help_text="Действие, которое представляет собой привычка",
    )

    is_pleasant = models.BooleanField(
        verbose_name="Признак приятной привычки",
        help_text="Признак приятной привычки",
        blank=True,
        null=True,
    )

    related_pleasant_habit = models.ForeignKey(
        "Habit",
        on_delete=models.SET_NULL,
        verbose_name="Связанная приятная привычка",
        related_name="useful_habits",
        null=True,
        blank=True,
    )

    periodicity = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность в днях",
    )

    reward = models.TextField(
        verbose_name="Вознаграждение за выполнение",
        help_text="Вознаграждение за выполнение",
        null=True,
        blank=True,
    )

    execution_time = models.PositiveIntegerField(
        default=120,
        verbose_name="Время на выполнение в секундах",
    )

    is_public = models.BooleanField(
        verbose_name="Признак публичности",
        help_text="Признак публичности",
        default=False,
    )

    created_at = models.DateTimeField(
        verbose_name="Дата/время создания", auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата/время обновления", auto_now=True
    )

    def __str__(self):
        return f"{self.action} {self.time} {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["id"]
