import random
import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден! Добавь BOT_TOKEN в Environment Variables.")

bot = telebot.TeleBot(TOKEN)

user_state = {}

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
    "Ммм мясо",
    "А пососать?", 
    "А ты знаешь что нужно делать с лживым гавном?", 
    "Розбань", 
    "База",
    "Фу",
    "Извинись перед моей мамой",
    "Бред",
    "Кидай голый кружок с извинениями",
    "Ты женщина?", 
    "Ты девочка или мальчик?"
]

@bot.message_handler(content_types=['text'])
def handle_message(message):
    user_id = message.from_user.id
    text = message.text.lower().strip()
    original_text = message.text.strip()  # ← ВОТ ЭТА СТРОЧКА БЫЛА ПРОПУЩЕНА!

    # Проверка: ждём ли мы ответа
    if user_id in user_state:
        question_type = user_state[user_id]
        del user_state[user_id]
        
        if question_type == "woman":
            if text in ["да", "да.", "да!"]:
                bot.reply_to(message, "Кидай кружок")
                return
        elif question_type == "girl_or_boy":
            if text in ["девочка", "девушка", "женщина"]:
                bot.reply_to(message, "Кидай кружок")
                return

    # 1. Проверка на "сам"
    if text == "сам":
        bot.reply_to(message, "Ооо, стрелки пошли")
        return

    # 2. Проверка на "бог" с маленькой буквы
    words_original = original_text.split()
    if "бог" in words_original:
        bot.reply_to(message, "Бог с большой*")
        return

    # 3. Проверка на маты
    bad_words = ["бля", "блять", "блядь", "хуй", "пизда", "еба", "ебать", "ебля", "сука", "нах", "нахуй", "залупа", "мудак", "гандон", "пидор", " пидар", "долбоеб", "долбаеб", "уебан", "еблан", "выебан", "хуйло", "хуесос"]
    if any(word in text for word in bad_words):
        bot.reply_to(message, random.choice(["Без матов чурка", "Без матов существо"]))
        return

    # 4. Проверка на "жир"
    if any(word in text for word in ["жир", "жыр", "жырны", "жирный"]):
        bot.reply_to(message, "Я не жирный")
        return

    # 5. Проверка на "чурка"
    if "чурка" in text:
        bot.reply_to(message, random.choice(["У меня белая кожа", "Ооо, кидай кожу"]))
        return

    # 6. Проверка на "пдф" или "педофил"
    if "пдф" in text or "педофил" in text:
        bot.reply_to(message, "что плохого в пдф?")
        return

    bot.reply_to(message, random.choice(PHRASES))

print("Бот запущен на Render!")
bot.infinity_polling()
