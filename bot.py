import random
import telebot
import os

# Токен Render будет брать из переменных окружения
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Токен не найден! Добавь BOT_TOKEN в Environment Variables на Render.")

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

print("Бот запущен на Render!")
bot.infinity_polling()
