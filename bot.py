import random
import telebot

# ВСТАВЬТЕ ТОКЕН СЮДА
TOKEN = "8775278436:AAFuOV-1C66uSUg3TfofThoiVq0ERPKf8PI"

bot = telebot.TeleBot(TOKEN)

PHRASES = [
    "Отвечай за нахрюк",
    "Самый умный либерал:",
    "Ха хп ха",
    "Нахрюкал",
    "Копиум",
    "Мясо",
    "Самый натурал прозападник наци яз:",
    "Без матов чурка",
    "Ты женщина?",
    "Кидай кожу",
    "Кидай живот",
    "Кидай голый кружок с извинениями",
    "База",
]

@bot.message_handler(content_types=['text'])
def send_random(message):
    answer = random.choice(PHRASES)
    bot.reply_to(message, answer)

print("Бот запущен! Напишите ему в Telegram.")
bot.infinity_polling()
