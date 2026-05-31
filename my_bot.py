import telebot
import random

TOKEN = "8736361524:AAHDQ2SBL2fmHrKp_wJuP8uc7ultBDB85c4"

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
bot.remove_webnook()
print("ربات روشن شد...")
bot.infinity_polling()
