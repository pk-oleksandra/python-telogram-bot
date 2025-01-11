import telebot

token = '8165258753:AAE1VHyPrE1yc3iSq54jY7u4ddU2cilA_vk'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def say_bot(message):

    if isInt(message.text):
        with open ('f1.tx', 'a')as file:
            file.write(message.text + '\n')
    else:
        with open('f2.txt', 'a') as file:
            file.write(message.text + '\n')
    bot.send_message(message.chat.id, "ok!")


if __name__=='__main__':
    bot.polling()