from telebot import TeleBot, types
from config import token
# import os


# token = os.getenv('TOKEN')
bot = TeleBot(token)


# texts for greetings and list of available commands.
commands_list = """
Ось список доступних команд чат-бота:
/help - Показує усі доступні команди.
/list - Показує список доступних тем.
\n
"""
greeting_text = 'Привіт! Цей бот допоможе вам знайти статті по темі, \
яка вас цікавить. \n'
notice_text = 'Клавіатуру можна скрити чи показати по кліку на клавіатуру \
у правому куті поля для вводу текста.\n'


# Articles and their urls.
topics_links = {
    "робота": {"link_1": "http://www.some_url_1",
               "link_2": "http://www.some_url_2"},
    "освіта": {"link_3": "http://www.some_url_3",
               "link_4": "http://www.some_url_4"},
    "медицина": {"link_5": "http://www.some_url_3",
                 "link_6": "http://www.some_url_4"},
}


###############################################################################
#                                           Block Keyboards                   #
###############################################################################


# returns main menu keyboard with commands
def menu_keyboard():
    menu_keyboard = types.ReplyKeyboardMarkup()
    btn_help = types.KeyboardButton('/help')
    btn_list = types.KeyboardButton('/list')

    menu_keyboard.row(btn_help, btn_list)
    return menu_keyboard


def topics_keyboard():
    topics_keyboard = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Робота')
    itembtn2 = types.KeyboardButton('Освіта')
    itembtn3 = types.KeyboardButton('Медицина')
    topics_keyboard.add(itembtn1, itembtn2, itembtn3)
    return topics_keyboard


############################################################################
#                   Commands and message handling                          #
############################################################################


@bot.message_handler(commands=['start'])
def command_start(message):
    keyboard = menu_keyboard()
    bot.send_message(message.chat.id,
                     greeting_text+notice_text+commands_list,
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, commands_list)


@bot.message_handler(commands=['list'])
def command_list(message):
    keyboard = topics_keyboard()
    bot.send_message(message.chat.id,
                     "Будь ласка оберіть тему",
                     reply_markup=keyboard)


@bot.message_handler(content_types='text')
def message_reply(message):
    topic = message.text.strip().lower()
    if topic in topics_links:
        reply_text = "Усі статті по темі: \n"
        for k, v in topics_links.get(topic).items():
            reply_text += f"{k} - {v}\n"
    else:
        reply_text = "Такої теми не існує"
    bot.send_message(message.chat.id, reply_text)


if __name__ == '__main__':
    bot.polling()
