from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from config import news_pattern, sale_pattern, EVENT_WORD
from db import db_conn

FILTERED = True


def start(bot: Bot, update: Update):
    reply_keyboard = [["/news", "/sales"]]
    update.message.reply_text(
        "Выберите команду:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )


def five_last_news(bot: Bot, update: Update):
    news = [
        news_pattern.format(title=title, body=body, date=date)
        for title, body, date in
        db_conn.execute("SELECT `header`, `news_text`, `date` FROM news ORDER BY date DESC LIMIT 5;")
    ]
    update.effective_chat.send_message('\n'.join(news))


def sales(bot: Bot, update: Update):
    keyboard = [
        [
            InlineKeyboardButton(
                sale_pattern.format(
                    _for=_for,
                    header=header,
                    what=what,
                ),
                callback_data=_for
            )
        ]
        for _for, header, what in
        db_conn.execute("SELECT DISTINCT `for`, `header`, `what` FROM sales;")
    ]

    reply_markup = InlineKeyboardMarkup(keyboard, parse_mode='Markdown')
    update.message.reply_text('Sales:', reply_markup=reply_markup)


def sale(bot: Bot, update: Update):
    global FILTERED

    query = update.callback_query
    chosen_for = query.data

    FILTERED = not FILTERED

    not_filtered_query = "SELECT DISTINCT `for`, `header`, `what` FROM sales"
    filtered_query = f"SELECT DISTINCT `for`, `header`, `what` FROM sales WHERE `for` = '{chosen_for}';"

    final_query = not_filtered_query if FILTERED else filtered_query

    keyboard = [
        [
            InlineKeyboardButton(
                sale_pattern.format(
                    _for=_for,
                    header=header,
                    what=what,
                ),
                callback_data=_for
            )
        ]
        for _for, header, what in
        db_conn.execute(final_query)
    ]

    query.edit_message_text(text='Sales:', reply_markup=InlineKeyboardMarkup(keyboard))
    query.answer(EVENT_WORD)
