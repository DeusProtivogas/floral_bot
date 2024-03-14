from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from .bot_handlers import welcome_pdf_user, not_accept_personal_data, ask_occasion, ask_price, show_example_bouqet, \
    order_courier_address, order_courier_name, order_courier_date, order_courier_time, order_courier_message, \
    ask_consultation, cosultation_requested


# def greet_user(update, context):
#     print('Вызван /start')
#
# def greet_user_1(update, context):
#     print('Вызван 111111 /start')


class Command(BaseCommand):
    help = 'Телеграм Бот'

    def handle(self, *args, **options):
        updater = Updater(settings.TG_TOKEN, use_context=True)

        dp = updater.dispatcher
        dp.add_handler(CommandHandler('start', welcome_pdf_user))

        dp.add_handler(MessageHandler(Filters.regex('^(Не принимаю)$'), not_accept_personal_data))
        # dp.add_handler(MessageHandler(Filters.regex('^(Принимаю)$'), ask_occasion))


        # master_name = update.message.text
        # context.user_data["order"]["master"] = master_name

        ordering = ConversationHandler(
            entry_points=[
                MessageHandler(Filters.regex('^(Принимаю)$'), ask_occasion),
                # MessageHandler(Filters.location, booking_gave_location),
            ],
            states={
                # "start": [MessageHandler(Filters.text, greet_user)],
                "ask_occasion": [MessageHandler(Filters.text, ask_occasion)],
                "choose_price": [MessageHandler(Filters.text, ask_price)],
                "show_example": [MessageHandler(Filters.text, show_example_bouqet)],
                "order_choice": [
                    MessageHandler(Filters.regex('Заказать'), order_courier_name),
                    # MessageHandler(Filters.regex('Показать еще'), booking_method_2),
                    MessageHandler(Filters.regex('Консультация'), ask_consultation),
                    MessageHandler(Filters.regex('На главную'), ask_occasion),
                ],
                "order_courier_address": [MessageHandler(Filters.text, order_courier_address)],
                "order_courier_date": [MessageHandler(Filters.text, order_courier_date)],
                "order_courier_time": [MessageHandler(Filters.text, order_courier_time)],
                "order_courier_message": [MessageHandler(Filters.text, order_courier_message)],

                "cosultation_requested": [MessageHandler(Filters.text, cosultation_requested)],
            },
            fallbacks=[]
        )
        dp.add_handler(ordering)



        updater.start_polling()
        updater.idle()