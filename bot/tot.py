import telebot

API_TOKEN = '7674978957:AAGe2zFfpmFJEIP418rVxn8y41vC3qlqXgc'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот TOT от команды ITshechka.")
    bot.send_message(message.chat.id, "Вы можете открыть наше Telegram-Mini-App по кнопке слева от чата. Желаем приятного пользования нашим приложением!")

if __name__ == '__main__':
    bot.polling()