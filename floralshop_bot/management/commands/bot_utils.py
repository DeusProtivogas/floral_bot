import re
from telegram import ReplyKeyboardMarkup

def is_possible_name(input_string):
    pattern = r'^[A-ZА-Я][a-zа-я]*(?:-[A-ZА-Я][a-zа-я]*)? [A-ZА-Я][a-zа-я]*(?:-[A-ZА-Я][a-zа-я]*)?$'

    if re.match(pattern, input_string):
        return True
    else:
        return False


def is_proper_date_format(input_string):
    pattern = r'^(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])$'

    if re.match(pattern, input_string):
        return True
    else:
        return False


def is_proper_time_format(input_string):
    pattern = r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'

    if re.match(pattern, input_string):
        return True
    else:
        return False


def personal_data_keyboard():
    return ReplyKeyboardMarkup([
        ['Принимаю', 'Не принимаю'],
    ], resize_keyboard=True)

def choose_occasion_keyboard():
    return ReplyKeyboardMarkup([
        ['Свадьба', 'День рождения']
    ],
        resize_keyboard=True
    )

def choose_price_keyboard():
    return ReplyKeyboardMarkup([
        ['1000', '3000', '5000']
    ],
        resize_keyboard=True
    )


def order_keyboard():
    return ReplyKeyboardMarkup([
        ['Заказать', 'Показать еще'],
        ['Консультация', 'На главную']
    ],
        resize_keyboard=True
    )

def return_to_main_keyboard():
    return ReplyKeyboardMarkup([
        ['На главную']
    ],
        resize_keyboard=True
    )

