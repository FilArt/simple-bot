from telegram.ext import CommandHandler, CallbackQueryHandler

from actions import start, sale, sales, five_last_news

start_handler = CommandHandler('start', start)
news_handler = CommandHandler('news', five_last_news)
sales_handler = CommandHandler('sales', sales)
sale_handler = CallbackQueryHandler(sale)
