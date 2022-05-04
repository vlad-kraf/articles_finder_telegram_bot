from telebot import TeleBot, types
#from config import token
import os
from content import topics_links


token = os.getenv('TOKEN')
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
    topics_keyboard = types.ReplyKeyboardMarkup(row_width=2)
    
    topics_keyboard.add(types.KeyboardButton('Документи для в\'їзду в Ірландію'),
                        types.KeyboardButton('Документи, які вам потрібні в Ірландії'),
                        types.KeyboardButton('Робота'),
                        types.KeyboardButton('Медицина'),
                        types.KeyboardButton('Психологічна підтримка'),
                        types.KeyboardButton('Як перевезти тварину в Ірландію'),
                        types.KeyboardButton('Де, та що купувати в Ірландії'),
                        types.KeyboardButton('Громадський транспорт'),
                        types.KeyboardButton('Мені потрібна допомога'),
                        types.KeyboardButton('В мене ще є питання'),
                        types.KeyboardButton('Чати, канали та інші корисні ресурси'),
                        types.KeyboardButton('Вивчення англійської'),
                        types.KeyboardButton('Освіта для дітей'),
                        types.KeyboardButton('Як дістатися до Ірландії'),
                        types.KeyboardButton('Соціальні виплати'),
                        types.KeyboardButton('Проживання'),
                        types.KeyboardButton('Державні ресурси'),
                        types.KeyboardButton('Що подивитись в Дубліні'))
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
