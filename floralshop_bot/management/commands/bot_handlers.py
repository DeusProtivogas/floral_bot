from .bot_utils import personal_data_keyboard, choose_occasion_keyboard, choose_price_keyboard


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
    update.message.reply_text(message)
    return -1

