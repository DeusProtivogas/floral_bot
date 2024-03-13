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