from telebot import TeleBot, types
from config import token
# import os
from content import topics_links


# token = os.getenv('TOKEN')
bot = TeleBot(token)


# texts for greetings and list of available commands.
greeting_text = 'Привіт! Цей бот допоможе вам знайти статті по темі, \
яка вас цікавить. \n'


###############################################################################
#                                           Block Keyboards                   #
###############################################################################

def topics_keyboard():
    topics_keyboard = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Документи для в\'їзду в Ірландію')
    itembtn2 = types.KeyboardButton('Документи, які вам потрібні в Ірландії')
    itembtn3 = types.KeyboardButton('Медицина')
    itembtn4 = types.KeyboardButton('Медицина')
    itembtn5 = types.KeyboardButton('Медицина')
    itembtn6 = types.KeyboardButton('Медицина')
    itembtn7 = types.KeyboardButton('Медицина')
    itembtn8 = types.KeyboardButton('Медицина')
    itembtn9 = types.KeyboardButton('Медицина')
    itembtn10 = types.KeyboardButton('Медицина')
    itembtn11 = types.KeyboardButton('Медицина')
    itembtn12 = types.KeyboardButton('Медицина')
    topics_keyboard.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12)
    return topics_keyboard



############################################################################
#                   Commands and message handling                          #
############################################################################


@bot.message_handler(commands=['start'])
def command_start(message):
    keyboard = topics_keyboard()
    bot.send_message(message.chat.id,
                     greeting_text,
                     reply_markup=keyboard)


@bot.message_handler(commands=['list'])
def command_list(message):
    keyboard = topics_keyboard()
    bot.send_message(message.chat.id,
                     "Будь ласка оберіть тему",
                     reply_markup=keyboard)


@bot.message_handler(content_types='text')
def message_reply(message):
    topic = message.text.strip().lower()
    reply_text = ""
    if topic in topics_links:
        reply_text += topics_links[topic]
    else:
        reply_text = "Такої теми чи команди чата не існує"
    
    bot.send_message(message.chat.id, reply_text, parse_mode='MarkdownV2', disable_web_page_preview=True)




if __name__ == '__main__':
    bot.polling()
