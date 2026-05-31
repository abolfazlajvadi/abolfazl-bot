import telebot
import os
import random

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات من خوش اومدی 👋")

@bot.message_handler(commands=['fale'])
def fortune(message):
    fale_ha = ["روزت عالی خواهد بود 🌟", "مراقب باش امروز ⚠️", "خبر خوبی بهت می‌رسه 📨", "یه اتفاق قشنگ امروز میافته 🎈"]
    bot.reply_to(message, random.choice(fale_ha))

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# ========== درست سر جای خودش ==========
bot.remove_webhook()   # <--- این خط باید اینجا باشد، نه داخل تابع
# ======================================

print("ربات روشن شد...")
bot.infinity_polling(none_stop=True)
