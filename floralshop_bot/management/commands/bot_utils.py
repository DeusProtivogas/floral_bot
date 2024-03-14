from telegram import ReplyKeyboardMarkup


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

