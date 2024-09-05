from celery import shared_task

from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_habit_notifications():
    users = User.objects.filter(tg_chat_id__isnull=False)
    for user in users:
        habits = user.habits.filter(is_pleasant__isnull=True)
        if habits.count():
            send_telegram_message(user.tg_chat_id, f"Привет, напоминаю о твоих привычках: {', '.join([str(habit) for habit in habits.all()])}.")
