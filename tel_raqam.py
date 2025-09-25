import telebot
from telebot import types

TOKEN = '8461672342:AAG7pd9e0V-SoJghCPGLh3BDS2WzLdY3TGU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True)
    markup.add(button)
    bot.send_message(message.chat.id, "Iltimos, telefon raqamingizni yuboring:", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact is not None:
        phone_number = message.contact.phone_number
        user_id = message.contact.user_id
        first_name = message.contact.first_name
        last_name = message.contact.last_name or ""

        # Ma'lumotlarni saqlash yoki ko'rsatish
        bot.send_message(
            message.chat.id,
            f"✅ Raqamingiz qabul qilindi!\n"
            f"📞 Telefon: {phone_number}\n"
            f"👤 Ism: {first_name} {last_name}\n"
            f"🆔 Telegram ID: {user_id}"
        )

        # Bu yerda siz ma'lumotni bazaga yozishingiz mumkin
        # Masalan: SQLite, PostgreSQL, JSON fayl, va h.k.

bot.polling()