# Generated by Django 4.2 on 2024-09-02 16:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        help_text="Место, в котором необходимо выполнять привычку",
                        max_length=255,
                        verbose_name="Место, в котором необходимо выполнять привычку",
                    ),
                ),
                (
                    "time",
                    models.CharField(
                        help_text="Время, в которое необходимо выполнять привычку",
                        max_length=255,
                        verbose_name="Время, в которое необходимо выполнять привычку",
                    ),
                ),
                (
                    "action",
                    models.TextField(
                        help_text="Действие, которое представляет собой привычка",
                        verbose_name="Действие, которое представляет собой привычка",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        blank=True,
                        help_text="Признак приятной привычки",
                        null=True,
                        verbose_name="Признак приятной привычки",
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Периодичность в днях"
                    ),
                ),
                (
                    "reward",
                    models.TextField(
                        blank=True,
                        help_text="Вознаграждение за выполнение",
                        null=True,
                        verbose_name="Вознаграждение за выполнение",
                    ),
                ),
                (
                    "execution_time",
                    models.PositiveIntegerField(
                        default=120, verbose_name="Время на выполнение в секундах"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False,
                        help_text="Признак публичности",
                        verbose_name="Признак публичности",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата/время создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата/время обновления"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="habits",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "related_pleasant_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="useful_habits",
                        to="habits.habit",
                        verbose_name="Связанная приятная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ["id"],
            },
        ),
    ]
