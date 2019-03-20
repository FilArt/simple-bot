from telegram.ext import Updater

from secrets import TOKEN
from handlers import sales_handler, start_handler, sale_handler, news_handler

updater = Updater(token=TOKEN)


def main():
    dispatcher = updater.dispatcher

    dispatcher.add_handler(sale_handler)
    dispatcher.add_handler(sales_handler)
    dispatcher.add_handler(news_handler)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
