from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Updater

# Ваш токен бота
BOT_TOKEN = "7901063068:AAFL955WOGlXooiiMXDWmv_N0LSgi5B-JrM"

# URL вашего Telegram Mini App
WEB_APP_URL = "https://example.com"  # Замените на свой адрес

def start(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton(
                text="Открыть Mini App", web_app={"url": WEB_APP_URL}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        text="Привет! Нажми на кнопку ниже, чтобы открыть наше приложение!",
        reply_markup=reply_markup
    )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
