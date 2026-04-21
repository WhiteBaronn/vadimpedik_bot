import random
import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден! Добавь BOT_TOKEN в Environment Variables.")

bot = telebot.TeleBot(TOKEN)

# === СЛОВАРЬ СЛУЧАЙНЫХ ФРАЗ ===
PHRASES = [
    "Самый умный либерал:",
    "Самый натурал западник:",
    "Самый мудрый наци яз:",
    "Самы умный нахрюкер:",
    "Отвечай за нахрюк",
    "Ответь за нахрюк",
    "Нет 😁 отвечай за нахрюк",
    "Нахрюкал",
    "Не хрюкай",
    "Нахрюк не спасет",
    "Опять нахрюк",
    "Нахрюк классик",
    "Ну и сразу нахрюк",
    "Руны не спасут",
    "Ха хп ха",
    "Ха ха ха",
    "Копиум",
    "Копиум пошел",
    "Копиум дикий",
    "Копиум классика",
    "Кидай кожу",
    "Кидай живот",
    "Мясо",
    "База",
    "Фу",
    "Извинись перед моей мамой",
    "Бред",
    "Кидай голый кружок с извинениями", 
    "Ты женщина?",
    "Ты мальчик или девочка?"
]

# === ОБРАБОТЧИК СООБЩЕНИЙ ===
@bot.message_handler(content_types=['text'])
def handle_message(message):
    text = message.text.lower().strip()
    chat_id = message.chat.id

    # 1. Проверка на "сам"
    if text == "сам":
        bot.reply_to(message, "Ооо, стрелки пошли")
        return

        # 2. Проверка на "бог" с маленькой буквы (в оригинале)
    words_original = original_text.split()
    if "бог" in words_original:
        bot.reply_to(message, "Бог с большой*")
        return
        
    # 3. Проверка на маты (список ключевых слов)
    bad_words = ["бля", "блять", "блядь", "хуй", "пизда", "еба", "ебать", "ебля", "сука", "нахуй", "нах", "залупа", "мудак", "гандон", "пидор", "долбоеб", "долбаеб", "уебан", "еблан", "выебан", "хуйло"]
    if any(word in text for word in bad_words):
        bot.reply_to(message, random.choice(["Без матов чурка", "Без матов существо"]))
        return

    # 4. Проверка на "жир", "жыр", "жырны", "жирный"
    if any(word in text for word in ["жир", "жыр", "жырны", "жирный"]):
        bot.reply_to(message, "Я не жирный")
        return

    # 5. Проверка на "чурка"
    if "чурка" in text:
        bot.reply_to(message, random.choice(["У меня белая кожа", "Ооо, кидай кожу"]))
        return

    # 6. Проверка на "пдф" или "педофил"
    if "пдф" in text or "педофил" in text:
        bot.reply_to(message, "Что плохого в пдф?")
        return

    # 8. Если ничего не подошло — случайная фраза
    bot.reply_to(message, random.choice(PHRASES))

# === ЗАПУСК ===
print("Бот с новыми фразами запущен на Render!")
bot.infinity_polling()
