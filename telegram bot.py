import telebot

bot = telebot.TeleBot("1449912361:AAEtNTEYDxUo5H6a_pQod3ItJ9ndY7qrc5I")


@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])


bot.polling()
