import telebot
import random

bot = telebot.TeleBot("1449912361:AAEtNTEYDxUo5H6a_pQod3ItJ9ndY7qrc5I")


@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    guesses_made = 0
    number = random.randint(1, 30)
    id = message.chat.id
    bot.send_message(id,"Привет, я загадал число между 1 и 30. Сможешь угадать?")


bot.polling()
