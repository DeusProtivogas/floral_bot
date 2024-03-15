from telegram import ReplyKeyboardRemove
from telegram.ext import Updater

import json
import phonenumbers

from floralshop import settings
from .bot_utils import personal_data_keyboard, choose_occasion_keyboard, choose_price_keyboard, order_keyboard, \
    return_to_main_keyboard


def welcome_pdf_user(update, context):

    chat_id = update.effective_chat.id
    with open('static/test.pdf', 'rb') as pdf_file:
        context.bot.send_document(chat_id=chat_id, document=pdf_file)
        welcome_pdf_message = 'Приветствуем в нашем боте. Перед использованием необходимо принять согласие на обработку ПД'
        update.message.reply_text(welcome_pdf_message, reply_markup=personal_data_keyboard())


def not_accept_personal_data(update, context):
    welcome_pdf_message = 'Извините без принятого согласия невозможно продолжить работу'
    update.message.reply_text(welcome_pdf_message, reply_markup=personal_data_keyboard())


def ask_occasion(update, context):
    is_first_bouquet = True
    context.user_data["is_first_bouquet"] = is_first_bouquet

    message = "К какому событию готовимся? Выберите один из вариантов:"
    update.message.reply_text(message, reply_markup=choose_occasion_keyboard())
    return "choose_price"


def ask_price(update, context):
    occasion = update.message.text
    context.user_data["occasion"] = occasion

    message = "На какую сумму рассчитываете?"
    update.message.reply_text(message, reply_markup=choose_price_keyboard())
    return "show_example"

TEST_BOUQETS = [
    {
        "description": "Text text text text\nText Text",
        "name": "bouqet_1",
        "composition": [
            "Flower 1",
            "Flower 2",
        ],
        "price": 500,
        "occasion": "Свадьба",
    },

    {
        "description": "Text text text",
        "name": "bouqet_2",
        "composition": [
            "Flower 1",
            "Flower 2",
            "Flower 3",
        ],
        "price": 1500,
        "occasion": "День рождения",
    },

    {
        "description": "Text text\nText Text",
        "name": "bouqet_3",
        "composition": [
            "Flower 1",
            "Flower 5",
            "Flower 3",
        ],
        "price": 2500,
        "occasion": "День рождения",
    },
{
        "description": "Text text text text\nText Text",
        "name": "bouqet_4",
        "composition": [
            "Flower 1",
            "Flower 2",
        ],
        "price": 1500,
        "occasion": "Свадьба",
    },
{
        "description": "Text text text text\nText Text",
        "name": "bouqet_DEF",
        "composition": [
            "Flower 1",
            "Flower 2",
        ],
        "price": 1500,
        "occasion": "Свадьба",
    },
]

def show_example_bouqet(update, context):
    if context.user_data["is_first_bouquet"]:
        context.user_data["is_first_bouquet"] = False
        price = update.message.text
        context.user_data["price"] = int(price)

        ###
        # Getting bouqet from a list
        ###
        context.user_data["bouqet"] = None
        for item in sorted(TEST_BOUQETS, key=lambda k: (k['occasion'].lower(), -k['price'])):
            print(item)
            if context.user_data["occasion"] == item['occasion'] and context.user_data["price"] < item['price']:
                context.user_data["bouqet"] = item
                break
        if not context.user_data["bouqet"]:
            context.user_data["bouqet"] = TEST_BOUQETS[-1]

        # Print example
        print(context.user_data["bouqet"])
        message = json.dumps(context.user_data["bouqet"])

    else:
        b_id = TEST_BOUQETS.index(context.user_data["bouqet"])
        context.user_data["bouqet"] = TEST_BOUQETS[(b_id + 1) % len(TEST_BOUQETS)]
        message = json.dumps(context.user_data["bouqet"])

    print("OCCASION: ", context.user_data["occasion"])
    print("PRICE: ", context.user_data["price"])
    print("is_first_bouquet: ", context.user_data["is_first_bouquet"])

    update.message.reply_text(message, reply_markup=order_keyboard())
    return "order_choice"


def order_courier_name(update, context):
    message = "Для заказа, пожалуйста введите имя:"
    update.message.reply_text(
        message,
        reply_markup = ReplyKeyboardRemove()
    )
    return "order_courier_address"


def order_courier_address(update, context):
    name = update.message.text
    context.user_data["name"] = name

    message = "Пожалуйста, введите адрес:"
    update.message.reply_text(
        message,
        reply_markup = ReplyKeyboardRemove()
    )
    return "order_courier_date"


def order_courier_date(update, context):
    address = update.message.text
    context.user_data["address"] = address

    message = "Пожалуйста, введите время доставки:"
    update.message.reply_text(
        message,
        reply_markup = ReplyKeyboardRemove()
    )
    return "order_courier_time"

def order_courier_time(update, context):
    date = update.message.text
    context.user_data["date"] = date

    message = "Пожалуйста, введите время доставки:"
    update.message.reply_text(
        message,
        reply_markup = ReplyKeyboardRemove()
    )
    return "order_courier_message"


def order_courier_message(update, context):
    time = update.message.text
    context.user_data["time"] = time

    message_to_courier = f"Новый заказ!\n" \
                         f"Имя: {context.user_data['name']}\n" \
                         f"Адрес: {context.user_data['address']}\n" \
                         f"Время: {context.user_data['time']}\n" \
                         f"Дата: {context.user_data['date']}\n"

    updater = Updater(settings.TG_TOKEN)
    updater.bot.sendMessage(chat_id=settings.COURIER_ID, text=message_to_courier)


    message = "Спасибо! Сообщаем курьеру!\nЕсли вы хотите заказать новый букет:"

    update.message.reply_text(
        message,
        reply_markup=return_to_main_keyboard(),
    )

    # return -1
    return "ask_occasion"

def ask_consultation(update, context):
    message = "Укажите номер телефона (В формате +7...), и наш флорист перезвонит вам в течение 20 минут"
    update.message.reply_text(
        message,
        reply_markup = ReplyKeyboardRemove(),
    )
    # print(update.message.text)
    # print(phonenumbers.is_possible_number(phonenumbers.parse(update.message.text)))

    return "cosultation_requested"

def cosultation_requested(update, context):
    phone = update.message.text
    context.user_data["phone"] = phone

    # print(update.message.text)

    try:
        # print(phonenumbers.is_possible_number(phonenumbers.parse(update.message.text)))

        message_to_consultant = f"Просят консультацию по номру: {phone}"

        updater = Updater(settings.TG_TOKEN)
        updater.bot.sendMessage(chat_id=settings.FLORIST_ID, text=message_to_consultant)

        message = "Спасибо! Скоро флорист свяжется с Вами!\nЕсли вы хотите заказать или посмотреть другие букеты:"

        update.message.reply_text(
            message,
            reply_markup=return_to_main_keyboard(),
        )

        # return -1
        return "ask_occasion"
    except phonenumbers.phonenumberutil.NumberParseException:
        message = "Извините, номер не правильный. Введит правильный номер:"

        update.message.reply_text(
            message,
            reply_markup = ReplyKeyboardRemove(),
        )

        # return -1
        return "cosultation_requested"

    #
    # message_to_consultant = f"Просят консультацию по номру: {phone}"
    #
    # updater = Updater(settings.TG_TOKEN)
    # updater.bot.sendMessage(chat_id=settings.FLORIST_ID, text=message_to_consultant)
    #
    # message = "Спасибо! Скоро флорист свяжется с Вами!\nЕсли вы хотите заказать или посмотреть другие букеты:"
    #
    # update.message.reply_text(
    #     message,
    #     reply_markup=return_to_main_keyboard(),
    # )
    #
    # # return -1
    # return "ask_occasion"