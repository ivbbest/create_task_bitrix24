from fast_bitrix24 import Bitrix
from datetime import datetime, timedelta
import requests
from config import WEBHOOK    # конфигурационный файл с вебхуком


def check_holiday_day():
    """
    Проверка, что за через 3 дня будет праздничный день
    """
    current_date = datetime.now().date()
    current_date_plus_3 = current_date + timedelta(days=2)
    resp = requests.get(f'https://isdayoff.ru/{current_date_plus_3}')

    return resp.text == '1'


def create_task(task):
    """
    Добавление задачи в Битрикс
    """
    webhook = WEBHOOK
    b = Bitrix(webhook)

    b.call('tasks.task.add', task)


def main():
    """
    Собираем 2 функции вместе
    """
    task = [
        {
            'ID': 1,
            'fields': {
                'TITLE': '3 New tasks in Bitrix',
                'RESPONSIBLE_ID': 1,
                'CREATED_BY': 1
            }
        }
    ]

    if check_holiday_day():
        create_task(task)


if __name__ == '__main__':
    main()
