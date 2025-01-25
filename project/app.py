import config as c
import telebot
import threading
import time
import sqlite3


bot = telebot.TeleBot(c.BOT_TOKEN)

USER_CHAT_ID = '516876967'

# === SQLITE3 =================================================================
db = sqlite3.connect(c.DB_NAME)
cursor = db.cursor()

cursor.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER NOT NULL UNIQUE,
    name TEXT DEFAULT 'Невідомий',
    deleted INTEGER DEFAULT 1
    )''')
db.commit()

cursor.execute('''CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT DEFAULT '',
    notification DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_send INTEGER DEFAULT 0, 
    deleted INTEGER DEFAULT 1
    )''')
db.commit()


# === FUNCTIONS ===============================================================
def send_stupid_message():
    while True:

        # ....

        bot.send_message(USER_CHAT_ID, '')
        time.sleep(10)


def bot_start(message):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()

    cur.execute(f"SELECT chat_id FROM user WHERE chat_id='{message.chat.id}'")
    row = cur.fetchone()

    if not row:
        cur.execute(f"INSERT INTO user (chat_id, name) VALUES ('{message.chat.id}', '{message.from_user.username}')")
        db.commit()
        bot.send_message(message.chat.id, 'Вас додано до цього бота!')
    else:
        bot.send_message(message.chat.id, 'Ви вже підписані на цього бота.')


# === HANDLER =================================================================

# start - підписка
# add - додати
# edit - редагувати
# del - видалити
# all - показати всі
# day - показати за день
# end - відписатися


# Обробник команд від користувача
@bot.message_handler(commands=['start', 'add', 'edit', 'del', 'all', 'day', 'end'])
def handler_commands(message):
    if '/start' == message.text:
        bot_start(message)
    elif '/add' == message.text:
        pass
    elif '/edit' == message.text:
        pass
    elif '/del' == message.text:
        pass
    elif '/all' == message.text:
        pass
    elif '/day' == message.text:
        pass
    elif '/end' == message.text:
        pass


# Обробник текстових повідомлень від користувача
@bot.message_handler(content_types=['text'])
def handler_text_message(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'БОТ Працює! ' + str(message.chat.id))


# if __name__ == "__main__":
#     # thread = threading.Thread(target=send_stupid_message)
#     # thread.start()
#     # Запуск бота
#     bot.infinity_polling()
