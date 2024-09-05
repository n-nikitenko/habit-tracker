import requests

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def send_telegram_message(chat_id, message):
    """Отправляет сообщение в телеграм"""

    params = {
        'text': message,
        'chat_id': chat_id,
    }
    try:
        requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params, timeout=5)
    except requests.exceptions.Timeout:
        print("Истекло время ожидания ответа сервера Телеграм.")  # todo: уточнить бизнес-логику
