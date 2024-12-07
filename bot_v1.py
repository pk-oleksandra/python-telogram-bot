import telebot
from telebot import types

token = '8165258753:AAE1VHyPrE1yc3iSq54jY7u4ddU2cilA_vk'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def say_number(message):
    if message.text == '1':
        request = 'Один'
    elif message.text == '2':
        request = 'Два'
    elif message.text == '3':
        request = 'Три'
    elif message.text == '4':
        request = 'Чотири'
    elif message.text == '5':
        request = 'Пять'
    else:
        request = ('Відповідь не знайдена')

    bot.send_message(message.chat.id, request)


if __name__ == '__main__':
    bot.polling()