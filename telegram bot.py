import telebot
import random

bot = telebot.TeleBot("1449912361:AAEtNTEYDxUo5H6a_pQod3ItJ9ndY7qrc5I")

@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    guesses_made = 0
    number = random.randint(1, 30)
    id = message.chat.id
    bot.send_message(id,"Привет, я загадал число между 1 и 30. Сможешь угадать?")
    inp = message.text.lower().split()
    for word in inp:
        guesses_made < 6
        guesses_made += 1
        if message < number:
            bot.send_message(id,"Твое число меньше того, что я загадал.")

        if message > number:
            bot.send_message(id,"Твое число больше загаданного мной.")

        if message == number:
            break

        if message == number:
            bot.send_message(id,"Ух ты, ! Ты угадал мое число, использовав  попыток!")
        else:
            bot.send_message(id, "А вот и не угадал! Я загадал число" )

bot.polling()
