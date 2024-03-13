from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from .bot_handlers import welcome_pdf_user, not_accept_personal_data, ask_occasion, ask_price, show_example_bouqet


def greet_user(update, context):
    print('Вызван /start')

def greet_user_1(update, context):
    print('Вызван 111111 /start')


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

        booking = ConversationHandler(
            entry_points=[
                MessageHandler(Filters.regex('^(Принимаю)$'), ask_occasion),
                # MessageHandler(Filters.location, booking_gave_location),
            ],
            states={
                # "start": [MessageHandler(Filters.text, greet_user)],
                "choose_price": [MessageHandler(Filters.text, ask_price)],
                "show_example": [MessageHandler(Filters.text, show_example_bouqet)]
            },
            fallbacks=[]
        )
        dp.add_handler(booking)



        updater.start_polling()
        updater.idle()