"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import timedelta, datetime

def print_days():
    # Сегодня
    today = datetime.now()
    print(f"Сегодня: {today}")

    # Вчера
    yesterday = today - timedelta(days=1)
    print(f"Вчера: {yesterday}")

    # 30 дней назад
    thirty_days_ago = today - timedelta(days=30)
    print(f"30 дней назад: {thirty_days_ago}")


def str_2_datetime(date_string):
    date_obj = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    print(f"Объект datetime: {date_obj}")

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
