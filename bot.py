import random
import telebot
import os
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден! Добавь BOT_TOKEN в Environment Variables.")
    
# === ФЕЙКОВЫЙ ВЕБ-СЕРВЕР ДЛЯ RENDER ===
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bot is running!')

    def log_message(self, format, *args):
        pass  # Не засоряем логи

def run_web_server():
    port = int(os.environ.get('PORT', 10000))
    server = HTTPServer(('0.0.0.0', port), HealthHandler)
    print(f"🌐 Веб-сервер запущен на порту {port}")
    server.serve_forever()

# Запускаем веб-сервер в отдельном потоке
threading.Thread(target=run_web_server, daemon=True).start()

bot = telebot.TeleBot(TOKEN)

# Получаем username бота для проверки пинга
bot_info = bot.get_me()
BOT_USERNAME = f"@{bot_info.username}".lower()

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
    original_text = message.text.strip()

    # === НОВАЯ ЛОГИКА: ПРОВЕРЯЕМ, НУЖНО ЛИ ОТВЕЧАТЬ ===
    should_reply = False
    
    # 1. Пинг (сообщение содержит @username_бота)
    if BOT_USERNAME in text:
        should_reply = True
    
    # 2. Ответ на сообщение бота (reply)
    if message.reply_to_message and message.reply_to_message.from_user.id == bot_info.id:
        should_reply = True
    
    # 3. Обычное сообщение — 5% шанс
    if not should_reply:
        if random.random() < 0.05:
            should_reply = True
        else:
            return  # Не отвечаем

    # === ДАЛЬШЕ ВАШ ОРИГИНАЛЬНЫЙ КОД БЕЗ ИЗМЕНЕНИЙ ===

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
    if "сам" in text:
        bot.reply_to(message, "Ооо, стрелки пошли")
        return

    # 2. Проверка на "бог" с маленькой буквы
    words_original = original_text.split()
    if "бог" in words_original:
        bot.reply_to(message, "Бог с большой*")
        return

    # 3. Проверка на маты
    bad_words = ["бля", "блять", "блядь", "хуй", "пизда", "еба", "ебать", "ебля", "сука", "нахуй", "залупа", "мудак", "гандон", "пидор", " пидар", "долбоеб", "долбаеб", "уебан", "еблан", "выебан", "хуйло", "хуесос"]
    if any(word in text for word in bad_words):
        bot.reply_to(message, random.choice(["Без матов чурка", "Без матов существо"]))
        return

    # 4. Проверка на "жир"
    if any(word in text for word in ["жир", "жыр", "жырны", "жирный"]):
        bot.reply_to(message, random.choice(["Я не жирный", " Мда, свин хрюкает про жир", "Одододо"]))
        return

    # 5. Проверка на "чурка"
    if "чурка" in text:
        bot.reply_to(message, random.choice(["У меня белая кожа", "Ооо, кидай кожу"]))
        return

    # 6. Проверка на "пдф" или "педофил"
    if "пдф" in text or "педофил" in text:
        bot.reply_to(message, random.choice(["Что плохого в пдф?", "Я христианин с пдф вайбом"]))
        return

    bot.reply_to(message, random.choice(PHRASES))

    bot.infinity_polling()
print("Бот запущен на Render!")

# === ЗАПУСК БОТА С АВТОРЕСТАРТОМ ===
while True:
    try:
        bot.infinity_polling(timeout=30, long_polling_timeout=10)
    except Exception as e:
        print(f"⚠️ Бот упал: {e}")
        print("🔄 Перезапуск через 10 секунд...")
        time.sleep(10)
