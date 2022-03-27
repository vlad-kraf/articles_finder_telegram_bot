from telebot import TeleBot, types
from config import token
# import os
from content import topics_links


# token = os.getenv('TOKEN')
bot = TeleBot(token)


# texts for greetings and list of available commands.
greeting_text = """Привіт\! 
Цей чат\-бот допоможе вам знайти статті по темі, яка вас цікавить \- просто оберіть потрібну категорію зі списку\. 
Якщо ви не знайшли те що шукали, будь ласка скористайтесь [зворотнім звʼязком](https://forms\.gle/qxUEtuRgr8vLxasW7) і ми постараємось доповнити інформацію найближчим часом\. 
Слава Україні\! 🇺🇦 """


###############################################################################
#                                           Block Keyboards                   #
###############################################################################

def topics_keyboard():
    topics_keyboard = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Документи для в\'їзду в Ірландію')
    itembtn2 = types.KeyboardButton('Документи, які вам потрібні в Ірландії')
    itembtn3 = types.KeyboardButton('Робота')
    itembtn4 = types.KeyboardButton('Медицина')
    itembtn5 = types.KeyboardButton('Психологічна підтримка')
    itembtn6 = types.KeyboardButton('Як перевезти тварину в Ірландію')
    itembtn7 = types.KeyboardButton('Де, та що купувати в Ірландії')
    itembtn8 = types.KeyboardButton('Громадський транспорт')
    itembtn9 = types.KeyboardButton('Мені потрібна допомога')
    itembtn10 = types.KeyboardButton('В мене ще є питання')
    itembtn11 = types.KeyboardButton('Чати, канали та інші корисні ресурси')
    itembtn12 = types.KeyboardButton('Медицина')
    itembtn13 = types.KeyboardButton('Медицина')
    itembtn14 = types.KeyboardButton('Медицина')
    itembtn15 = types.KeyboardButton('Медицина')
    itembtn16 = types.KeyboardButton('Медицина')
    itembtn17 = types.KeyboardButton('Медицина')
    itembtn18 = types.KeyboardButton('Зворотній зв’язок')
    topics_keyboard.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13, itembtn14, itembtn15, itembtn16, itembtn17, itembtn18)
    return topics_keyboard



############################################################################
#                   Commands and message handling                          #
############################################################################


@bot.message_handler(commands=['start'])
def command_start(message):
    keyboard = topics_keyboard()
    bot.send_message(message.chat.id,
                     greeting_text,
                     reply_markup=keyboard, 
                     parse_mode='MarkdownV2', 
                     disable_web_page_preview=True)


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
