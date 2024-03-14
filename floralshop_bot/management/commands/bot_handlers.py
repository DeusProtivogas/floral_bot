from telegram import ReplyKeyboardRemove
from telegram.ext import Updater

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
    message = "К какому событию готовимся? Выберите один из вариантов:"
    update.message.reply_text(message, reply_markup=choose_occasion_keyboard())
    return "choose_price"


def ask_price(update, context):
    occasion = update.message.text
    context.user_data["occasion"] = occasion

    message = "На какую сумму рассчитываете?"
    update.message.reply_text(message, reply_markup=choose_price_keyboard())
    return "show_example"

def show_example_bouqet(update, context):
    price = update.message.text
    context.user_data["price"] = price

    print("OCCASION: ", context.user_data["occasion"])
    print("PRICE: ", context.user_data["price"])

    message = "Пример букета " # TODO
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
    message = "Укажите номер телефона, и наш флорист перезвонит вам в течение 20 минут"
    update.message.reply_text(
        message,
        reply_markup = ReplyKeyboardRemove(),
    )

    return "cosultation_requested"

def cosultation_requested(update, context):
    phone = update.message.text
    context.user_data["phone"] = phone


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