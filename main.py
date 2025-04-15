import telebot
from flask import Flask, request
import os

TOKEN = os.environ.get("TOKEN")  # Убедись, что в Render переменная называется "TOKEN"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я Искра-бот, готов к службе.")

@app.route("/" + TOKEN, methods=["POST"])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://iskra-bot.onrender.com/' + TOKEN)
    return "Webhook set", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
