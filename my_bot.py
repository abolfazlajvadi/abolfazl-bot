import telebot
import os
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

# ----- دستورات ربات -----
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

# ----- سرور HTTP ساده برای Render (پورت 8000) -----
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_http_server():
    server = HTTPServer(('0.0.0.0', 8000), HealthCheckHandler)
    server.serve_forever()

# اجرای سرور HTTP در یک ترد جداگانه (همزمان با ربات)
http_thread = threading.Thread(target=run_http_server, daemon=True)
http_thread.start()

# ----- اجرای ربات -----
bot.remove_webhook()   # پاک کردن webhook قبلی
print("ربات روشن شد... (HTTP server on port 8000)")
bot.infinity_polling(none_stop=True)
