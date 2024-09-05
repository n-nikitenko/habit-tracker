from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """модель для пользователя"""

    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="Телеграм-ID чата",
        blank=True,
        null=True,
        help_text="Телеграм-ID чата, в который будут отправляться напоминания о выполнении привычки",
        unique=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
