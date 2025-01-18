import config
import telebot
import threading
import  time
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)


USER_CHAT_ID = '2139341372'

db = sqlite3.connect('notebook.db')
cursor = db.cursor()


cursor.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL,
    name TEXT DEFAULT 'Unknown',
    email TEXT DEFAULT '',
    role INTEGER DEFAULT 0,
    deleted INTEGER DEFAULT 1
    )''')
db.commit()

def send_stupid_message():
    while True:
        bot.send_message(USER_CHAT_ID, 'Дурненьке повідомлення')
        time.sleep(10)

@bot.message_handler(content_types=['text'])
def handler_text_message(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'БОТ Працює!' + str(message.chat.id))


if __name__ == "__main__":
    thread = threading.Thread(target=send_stupid_message)
    thread.start()
    bot.infinity_polling()
