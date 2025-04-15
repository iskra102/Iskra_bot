import telebot

# Bot token
TOKEN = '7503527452:AAGeEs1Xk0vAykJtIaxd42IkpWCjjS8qQM4'
bot = telebot.TeleBot(TOKEN)

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm Iskra, your assistant. Ready to help.")

# Echo any other message
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f'You said: {message.text}')

# Run the bot
if __name__ == '__main__':
    bot.infinity_polling()
