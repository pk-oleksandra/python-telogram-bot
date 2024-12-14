import telebot
from telebot import types

token = '7391689885:AAGK7dR_-29yZpr3NHfqT8C3RG5srr8cbUM'
bot = telebot.TeleBot(token)

# --- BOT MESSAGE ---------------------------------------------------

# кманда починається з символа: /tato, /mama
@bot.message_handler(commands=['tato', 'mama', 'b'])
def bot_commands(message):
    mes = ''

    if message.text == '/tato':
        mes = 'Тата нема дома'
    elif message.text == 'mama':
        mes = 'Мама зараз шиє'
    elif message.text == '/b':
        bot_buttons(message)
        return True

    bot.send_message(message.chat.id, mes)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    mes = message.text + ' - Це просто текст'
    bot.send_message(message.chat.id, mes)


# --- Функції -------------------------------------------------------

# Додаємо кнопки
def bot_buttons(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='Кнопка 1')
    button_2 = types.KeyboardButton(text='Кнопка 2')
    button_3 = types.KeyboardButton(text='Кнопка 3')
    button_4 = types.KeyboardButton(text='Кнопка 4')
    keyboard.add(button_1, button_2, button_3, button_4)

    msg = bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    bot.register_next_step_handler(msg, button_if)


def button_if(message):
    if message.text == 'Кнопка 1':

        # ... запустити програму ...
        bot.send_message(message.chat.id, '1. Закопати путіна')
    elif message.text == 'Кнопка 2':
        bot.send_message(message.chat.id, '2. Закопати шойгу')
    else:
        bot.send_message(message.chat.id, '3,4. запустити русоріз')


if __name__ == '__main__':
    bot.polling()
